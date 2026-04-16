"""
TASK: Get all NAT policies for the selected domain.

- GET /policy/ftdnatpolicies (pagination handled)
- Writes to outputs/<run>/get_nat_policies.<yaml|json>
"""

from fmc_orchestrator import BASE_URL, RunContext, fmc_get_all_items, write_output


def run(access_token: str, ctx: RunContext) -> None:
    url = f"{BASE_URL}/api/fmc_config/v1/domain/{ctx.domain_uuid}/policy/ftdnatpolicies"

    print("\n=== Fetching NAT policies ===")
    nat_policies = fmc_get_all_items(access_token, url)

    out_path = write_output(
        ctx,
        file_stem="get_nat_policies",
        payload=nat_policies,
    )
    print(f"Saved NAT policies -> {out_path}")
