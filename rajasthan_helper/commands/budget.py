"""Simple, transparent trip-budget allocation command."""

import click
from rich.console import Console
from rich.table import Table

console = Console()

# Planning shares, not quoted market prices. Users can edit the allocation mentally.
ALLOCATIONS = (
    ("Stay", 0.35),
    ("Food", 0.25),
    ("Local transport", 0.15),
    ("Activities", 0.15),
    ("Emergency buffer", 0.10),
)


@click.command()
@click.argument("total", type=click.IntRange(min=1))
@click.argument("days", type=click.IntRange(min=1))
def budget(total, days):
    """Split a total INR trip budget across DAYS (illustrative planning shares)."""
    table = Table(title=f"Trip budget · ₹{total:,} · {days} day(s)")
    table.add_column("Category", style="cyan")
    table.add_column("Suggested share", justify="right")
    table.add_column("Amount", justify="right", style="green")
    for label, share in ALLOCATIONS:
        table.add_row(label, f"{share:.0%}", f"₹{round(total * share):,}")
    console.print(table)
    console.print(f"Daily average: ₹{total / days:,.0f}/day")
    console.print(
        "[dim]Planning illustration only—not live prices or a cost guarantee. "
        "Adjust for travel mode, season, group size, bookings and actual quotes.[/dim]"
    )
