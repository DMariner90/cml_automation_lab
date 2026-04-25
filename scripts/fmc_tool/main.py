#!/usr/bin/env python3
"""
FMC TOOL MAIN (Interactive, Multi-Task Run)
==========================================

Flow:
1) Prompt for FMC credentials (username/password) – never stored
2) Authenticate once
3) List and select domain
4) Create ONE per-run output folder
5) Choose default output format (YAML default)
6) Loop:
     - Select task
     - Optionally override output format for that task
     - Run task (outputs saved into same run folder)
     - Log task execution
     - Ask whether to run another task
"""

from getpass import getpass

from fmc_orchestrator import (
    FMC_HOST,
    RunContext,
    append_run_log,
    create_run_folder,
    fmc_authenticate,
    fmc_list_domains,
    select_domain,
)

from tasks import (
    get_rules,
    get_network_objects,
    get_interfaces,
    get_nat_policies,
)


# ---------------------------------------------------------------------------
# User interaction helpers
# ---------------------------------------------------------------------------
def choose_task() -> str:
    """
    Present the user with a list of available tasks.
    """
    print("\n=== Select Task ===")
    print("1) Get all access rules for selected/all policies in this domain")
    print("2) Get all network objects for this domain")
    print("3) Get interfaces for selected/all devices in this domain")
    print("4) Get all NAT policies for this domain")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print("Please enter 1, 2, 3, or 4.")


def choose_output_format() -> str:
    """
    Choose output format for saved files.

    YAML is default because it is easier to read.
    JSON is useful for tooling / exact API fidelity.
    """
    print("\n=== Output format ===")
    print("1) YAML (default, easiest to read)")
    print("2) JSON")

    choice = input("Choose output format (press Enter for YAML): ").strip()

    if choice == "" or choice == "1":
        return "yaml"
    if choice == "2":
        return "json"

    print("Invalid choice; defaulting to YAML.")
    return "yaml"


def ask_yes_no(prompt: str, default_yes: bool = True) -> bool:
    """
    Simple yes/no prompt helper.
    """
    suffix = " [Y/n]: " if default_yes else " [y/N]: "
    answer = input(prompt + suffix).strip().lower()

    if answer == "":
        return default_yes
    return answer in ("y", "yes")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=== Cisco FMC Automation Toolkit ===")

    # 1) Credentials (secure input, never written to disk)
    username = input("Enter FMC username: ")
    password = getpass("Enter FMC password: ")

    # 2) Authenticate
    access_token = fmc_authenticate(username, password)

    # 3) Domain selection
    domains = fmc_list_domains(access_token)
    domain = select_domain(domains)

    domain_name = domain["name"]
    domain_uuid = domain["uuid"]

    # 4) Create per-run outputs folder (once per run)
    run_dir = create_run_folder(domain_name, domain_uuid)

    # 5) Create shared run context
    ctx = RunContext(
        output_format="yaml",  # default; may be changed by user
        run_dir=run_dir,
        domain_name=domain_name,
        domain_uuid=domain_uuid,
        fmc_host=FMC_HOST,
    )

    print(f"\nRun folder created:\n  {ctx.run_dir}\n")

    # 6) Choose default output format for this run
    ctx.output_format = choose_output_format()

    append_run_log(
        ctx,
        {
            "event": "run_started",
            "default_output_format": ctx.output_format,
        },
    )

    # 7) Task loop (multi-task per run)
    while True:
        task_choice = choose_task()

        # Allow per-task output format override
        if not ask_yes_no("Use default output format for this task?", default_yes=True):
            ctx.output_format = choose_output_format()

        # Dispatch task
        if task_choice == "1":
            append_run_log(
                ctx,
                {"task": "get_rules", "output_format": ctx.output_format},
            )
            get_rules.run(access_token, ctx)

        elif task_choice == "2":
            append_run_log(
                ctx,
                {"task": "get_network_objects", "output_format": ctx.output_format},
            )
            get_network_objects.run(access_token, ctx)

        elif task_choice == "3":
            append_run_log(
                ctx,
                {"task": "get_interfaces", "output_format": ctx.output_format},
            )
            get_interfaces.run(access_token, ctx)

        elif task_choice == "4":
            append_run_log(
                ctx,
                {"task": "get_nat_policies", "output_format": ctx.output_format},
            )
            get_nat_policies.run(access_token, ctx)

        print(f"\n✅ Task complete. Outputs saved in:\n  {ctx.run_dir}\n")

        # Another task?
        if not ask_yes_no("Run another task in the same run folder?", default_yes=True):
            append_run_log(ctx, {"event": "run_finished"})
            print("\nAll tasks complete. Exiting.")
            break


if __name__ == "__main__":
    main()
