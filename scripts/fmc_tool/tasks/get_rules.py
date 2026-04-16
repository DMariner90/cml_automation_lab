"""
TASK: Get all access rules for selected/all policies in this domain.

- Lists policies in selected domain
- User can select:
    - Enter / all => all policies
    - 1 / 1,3,5   => selected policies
- For each chosen policy:
    - GET access rules (pagination handled)
    - Write to outputs/<run>/get_rules__policy-<name>.<yaml|json>
"""

from fmc_orchestrator import (
    BASE_URL,
    RunContext,
    append_run_log,
    fmc_get_all_items,
    fmc_list_policies,
    select_policies,
    write_output,
)


def run(access_token: str, ctx: RunContext) -> None:
    policies = fmc_list_policies(access_token, ctx.domain_uuid)
    selected_policies, selection_note = select_policies(policies)

    # Log what the user selected for this task (good for multi-task runs)
    append_run_log(
        ctx,
        {
            "task": "get_rules",
            "policy_selection": selection_note,
            "output_format": ctx.output_format,
        },
    )

    for policy in selected_policies:
        policy_id = policy["id"]
        policy_name = policy["name"]

        url = (
            f"{BASE_URL}/api/fmc_config/v1/domain/"
            f"{ctx.domain_uuid}/policy/accesspolicies/{policy_id}/accessrules"
        )

        print(f"\n=== Fetching rules for policy: {policy_name} ({policy_id}) ===")
        rules = fmc_get_all_items(access_token, url)

        out_path = write_output(
            ctx,
            file_stem=f"get_rules__policy-{policy_name}",
            payload=rules,
        )

        print(f"Saved rules -> {out_path}")
