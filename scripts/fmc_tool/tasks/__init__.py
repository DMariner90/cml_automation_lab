"""
TASKS PACKAGE
=============

Each task module exposes:

    run(access_token: str, ctx: RunContext) -> None

Tasks write outputs into ctx.run_dir using the shared orchestrator writer.
"""
