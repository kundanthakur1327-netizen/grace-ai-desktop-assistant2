#!/usr/bin/env python3
"""
Grace - Personal AI Desktop Assistant
Version: 1.0.0
Author: Kudan Thakur

A command-based AI desktop assistant that helps you control your system,
manage files, open applications, and automate tasks.
"""

import os
import sys
from utils.colors import *
from utils.helpers import *
from commands.system_commands import execute_system_command
from commands.file_commands import execute_file_command
from commands.app_commands import execute_app_command
from commands.web_commands import execute_web_command

class Grace:
    """Main Grace Assistant Class"""
    
    def __init__(self):
        self.name = "Grace"
        self.version = "1.0.0"
        self.running = True
        self.command_history = []
        
    def display_welcome(self):
        """Display welcome banner"""
        print("\n")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                                                              ║")
        print("║          🌟 Welcome to Grace - Your AI Desktop Assistant  🌟 ║")
        print("║                                                              ║")
        print("║                 Version 1.0.0 - Ready to Assist             ║")
        print("║                                                              ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print()
        print_grace("Hello! I'm Grace, your personal desktop assistant.")
        print_grace("Type 'help' to see all available commands.")
        print_grace("Type 'about' to learn more about me.")
        print()
    
    def display_help(self):
        """Display help menu"""
        print_header("📚 Grace Command Reference")
        
        commands_info = {
            "System Commands": [
                ("system-info", "Display detailed system information"),
                ("pwd", "Show current working directory"),
                ("cd <path>", "Change to a different directory"),
                ("clear-screen", "Clear the terminal screen"),
                ("shutdown", "Shutdown your computer (with confirmation)"),
                ("restart", "Restart your computer (with confirmation)"),
            ],
            "File Commands": [
                ("create-folder <name>", "Create a new folder"),
                ("create-file <name>", "Create a new empty file"),
                ("delete-file <path>", "Delete a file (with confirmation)"),
                ("rename-file <old> <new>", "Rename a file"),
                ("search-file <name>", "Search for files by name"),
                ("list-files [path]", "List files in current or specified directory"),
                ("file-info <path>", "Get detailed file information"),
            ],
            "App & Web Commands": [
                ("open-app <name>", "Open an application (chrome, vscode, notepad, file-explorer)"),
                ("open-website <name>", "Open a website (google, youtube, gmail, github, etc.)"),
                ("open-url <url>", "Open a custom URL in your browser"),
            ],
            "Python Commands": [
                ("run-python-file <path>", "Execute a Python script"),
            ],
            "Utility Commands": [
                ("help", "Show this help menu"),
                ("about", "Learn about Grace"),
                ("history", "View command history"),
                ("exit", "Exit Grace"),
            ]
        }
        
        for category, commands in commands_info.items():
            print(f"\n{Colors.BRIGHT_CYAN}{category}:{Colors.RESET}")
            print("-" * 60)
            for cmd, description in commands:
                print(f"  {Colors.BRIGHT_GREEN}{cmd:<30}{Colors.RESET} {description}")
    
    def display_about(self):
        """Display information about Grace"""
        print_header("ℹ️  About Grace")
        print(f"""
{Colors.BRIGHT_CYAN}Grace - Personal AI Desktop Assistant{Colors.RESET}
{Colors.DIM}Version {self.version}{Colors.RESET}

{Colors.BRIGHT_YELLOW}What is Grace?{Colors.RESET}
Grace is your personal desktop assistant inspired by Jarvis from Iron Man.
She helps you control your computer system, manage files, open applications,
and automate tasks using simple text commands.

{Colors.BRIGHT_YELLOW}Key Features:{Colors.RESET}
  ✓ System control and information
  ✓ File and folder management
  ✓ Application and website launcher
  ✓ Python script execution
  ✓ Command history tracking
  ✓ Safety confirmations for dangerous operations
  ✓ Beautiful colored terminal interface

{Colors.BRIGHT_YELLOW}Future Features:{Colors.RESET}
  ◊ Voice input and output
  ◊ Wake word detection ("Hey Grace")
  ◊ AI-powered conversations
  ◊ Advanced PC automation
  ◊ Browser automation
  ◊ Memory system
  ◊ GUI interface

{Colors.BRIGHT_YELLOW}Creator:{Colors.RESET}
  Kudan Thakur
  GitHub: kundanthakur1327-netizenhey

{Colors.BRIGHT_YELLOW}Repository:{Colors.RESET}
  https://github.com/kundanthakur1327-netizenhey/grace-ai-desktop-assistant2

{Colors.DIM}Made with ❤️ to help you be more productive.{Colors.RESET}
        """)
    
    def display_history(self):
        """Display command history"""
        history = get_command_history()
        
        if not history:
            print_info("No command history yet.")
            return
        
        print_header("📜 Command History")
        for i, cmd in enumerate(history[-20:], 1):  # Show last 20 commands
            print(f"  {i:2d}. {cmd.strip()}")
    
    def parse_and_execute(self, user_input):
        """Parse user input and execute appropriate command"""
        
        user_input = user_input.strip()
        if not user_input:
            return
        
        # Log command to history
        log_command(user_input)
        self.command_history.append(user_input)
        
        # Split command and arguments
        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        # Utility Commands
        if command == "help":
            self.display_help()
        elif command == "about":
            self.display_about()
        elif command == "history":
            self.display_history()
        elif command == "exit":
            self.exit_grace()
        elif command == "clear-screen":
            clear_screen()
            self.display_welcome()
        
        # System Commands
        elif command in ["system-info", "pwd", "cd", "shutdown", "restart"]:
            execute_system_command(command, args)
        
        # File Commands
        elif command in ["create-folder", "create-file", "delete-file", "rename-file", 
                        "search-file", "list-files", "file-info"]:
            execute_file_command(command, args)
        
        # App Commands
        elif command in ["open-app", "run-python-file"]:
            execute_app_command(command, args)
        
        # Web Commands
        elif command in ["open-website", "open-url"]:
            execute_web_command(command, args)
        
        else:
            print_error(f"Unknown command: '{command}'. Type 'help' for available commands.")
    
    def exit_grace(self):
        """Exit Grace gracefully"""
        print()
        print_grace("Goodbye! Have a great day! 👋")
        self.running = False
        sys.exit(0)
    
    def run(self):
        """Main Grace loop"""
        self.display_welcome()
        
        while self.running:
            try:
                print_command_prompt()
                user_input = input()
                self.parse_and_execute(user_input)
            except KeyboardInterrupt:
                print("\n")
                print_grace("Interrupted. Type 'exit' to quit.")
            except Exception as e:
                print_error(f"An unexpected error occurred: {str(e)}")

def main():
    """Main entry point"""
    grace = Grace()
    grace.run()

if __name__ == "__main__":
    main()
