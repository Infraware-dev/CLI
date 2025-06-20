from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box

# Cloud providers configuration
CLOUD_PROVIDERS = [
    {"name": "GCP", "full_name": "Google Cloud Platform", "color": "bright_blue"},
    {"name": "AWS", "full_name": "Amazon Web Services", "color": "bright_blue"},
    {"name": "Azure", "full_name": "Microsoft Azure", "color": "bright_blue"},
    {"name": "Hetzner", "full_name": "Hetzner Cloud", "color": "bright_blue"},
    # Add more providers here as needed:
    # {"name": "Oracle", "full_name": "Oracle Cloud", "color": "bright_red"},
    # {"name": "IBM", "full_name": "IBM Cloud", "color": "bright_green"},
    # {"name": "Alibaba", "full_name": "Alibaba Cloud", "color": "bright_magenta"},
]


def create_providers_text(providers_list, use_full_names=False, show_icons=False):
    """Create a Text object with cloud providers from the configuration list."""
    providers_text = Text()

    if show_icons:
        providers_text.append("☁️  ", style="white")

    for i, provider in enumerate(providers_list):
        if i > 0:
            providers_text.append(
                " & " if not show_icons else "  •  ", style="bright_white"
            )

        name = provider["full_name"] if use_full_names else provider["name"]
        providers_text.append(name, style=f"bold {provider['color']}")

    if show_icons:
        providers_text.append("  ☁️", style="white")

    return providers_text


# Alternative version with even more styling
def print_banner():
    """Print an even more enhanced banner with animations and effects."""
    console = Console()

    # ASCII art with rainbow effect
    ascii_art = Text()
    ascii_lines = [
        "██╗███╗   ██╗███████╗██████╗  █████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗",
        "██║████╗  ██║██╔════╝██╔══██╗██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝",
        "██║██╔██╗ ██║█████╗  ██████╔╝███████║██║ █╗ ██║███████║██████╔╝█████╗  ",
        "██║██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║███╗██║██╔══██║██╔══██╗██╔══╝  ",
        "██║██║ ╚████║██║     ██║  ██║██║  ██║╚███╔███╔╝██║  ██║██║  ██║███████╗",
        "╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝",
    ]

    # Rainbow gradient
    colors = ["#1703C3", "#2B1BD1", "#3F33DF", "#534BED", "#6763FB", "#7B7BFF"]

    for i, line in enumerate(ascii_lines):
        ascii_art.append(line + "\n", style=colors[i % len(colors)])

    ascii_panel = Panel(
        Align.center(ascii_art), box=box.DOUBLE_EDGE, border_style="#1703C3"
    )

    # Cloud providers with icons using the configuration
    providers_text = create_providers_text(
        CLOUD_PROVIDERS, use_full_names=True, show_icons=True
    )

    providers_panel = Panel(
        Align.center(providers_text),
        title="[bold #2B1BD1]Supported Platforms[/]",
        box=box.ROUNDED,
        border_style="#1703C3",
    )

    # Status and commands
    status_text = Text()
    status_text.append("\nVersion: ", style="#2B1BD1 bold")
    status_text.append("Alpha", style="white")

    commands_text = Text()
    commands_text.append("Available Commands:\n", style="#2B1BD1 bold")
    commands_text.append("  • ", style="bright_white")
    commands_text.append("exit", style="#2B1BD1 bold")
    commands_text.append(" - Quit the application\n", style="white")

    info_panel = Panel(
        Text.assemble(status_text, "\n\n", commands_text),
        title="[bold #2B1BD1]System Information[/]",
        box=box.ROUNDED,
        border_style="#1703C3",
    )

    # Print everything with spacing
    console.print()
    console.print(ascii_panel)
    console.print()
    console.print(providers_panel)
    console.print()
    console.print(info_panel)
    console.print()
