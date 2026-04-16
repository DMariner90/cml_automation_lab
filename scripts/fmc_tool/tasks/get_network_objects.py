"""
TASK: Get all network objects for the selected domain.

- GET /object/networks (pagination handled)
- Writes to outputs/<run>/get_network_objects.<yaml|json>
"""

from fmc_orchestrator import BASE_URL, RunContext, fmc_get_all_items, write_output


def run(access_token: str, ctx: RunContext) -> None:
    url = f"{BASE_URL}/api/fmc_config/v1/domain/{ctx.domain_uuid}/object/networks"

    print("\n=== Fetching network objects ===")
    objects = fmc_get_all_items(access_token, url)

    out_path = write_output(
        ctx,
        file_stem="get_network_objects",
        payload=objects,
    )
    print(f"Saved network objects -> {out_path}")
