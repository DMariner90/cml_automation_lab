"""
TASK: Get interfaces for selected/all devices in the selected domain.

Flow:
- List devices in the domain (pagination handled)
- Select devices:
    - Enter / all => all devices
    - 1 / 1,3,5   => selected devices
- For each device:
    - GET operational interfaces
    - Write to outputs/<run>/get_interfaces__device-<name>.<yaml|json>
"""

from fmc_orchestrator import (
    BASE_URL,
    RunContext,
    append_run_log,
    fmc_get_all_items,
    fmc_list_devices,
    select_devices,
    write_output,
)


def run(access_token: str, ctx: RunContext) -> None:
    devices = fmc_list_devices(access_token, ctx.domain_uuid)
    selected_devices, selection_note = select_devices(devices)

    # Log selection + format for this task
    append_run_log(
        ctx,
        {
            "task": "get_interfaces",
            "device_selection": selection_note,
            "output_format": ctx.output_format,
        },
    )

    # Optional: always write an inventory snapshot for reference
    write_output(ctx, "device_inventory", devices)

    for dev in selected_devices:
        dev_id = dev["id"]
        dev_name = dev["name"]

        url = (
            f"{BASE_URL}/api/fmc_config/v1/domain/"
            f"{ctx.domain_uuid}/device/devicerecords/{dev_id}/operational/interfaces"
        )

        print(f"\n=== Fetching interfaces for device: {dev_name} ({dev_id}) ===")
        interfaces = fmc_get_all_items(access_token, url)

        out_path = write_output(
            ctx,
            file_stem=f"get_interfaces__device-{dev_name}",
            payload=interfaces,
        )
        print(f"Saved interfaces -> {out_path}")
