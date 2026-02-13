#!/data/data/com.termux/files/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import sys
from pathlib import Path

CONFIG_FILE = Path.home() / '.command_list.json'

def load_commands():
    """Load command list from file"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_commands(commands):
    """Save command list to file"""
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(commands, f, indent=2, ensure_ascii=False)

def clear_screen():
    """Clear terminal screen"""
    os.system('clear')

def show_menu():
    """Display interactive menu"""
    commands = load_commands()
    
    clear_screen()
    print("="*50)
    print("🚀 COMMAND MANAGER - INTERACTIVE MODE")
    print("="*50)
    
    if not commands:
        print("\n📝 No commands saved yet!")
    else:
        print("\n📋 Saved Commands:")
        for i, cmd in enumerate(commands, 1):
            print(f"  {i}. {cmd}")
    
    print("\n" + "-"*50)
    print("Options:")
    print("  [1-{}] - Run command by number".format(len(commands) if commands else 0))
    print("  [A] - Add new command")
    print("  [R] - Remove command")
    print("  [L] - List all commands")
    print("  [Q] - Quit")
    print("-"*50)

def add_command_interactive():
    """Interactive command addition"""
    print("\n➕ ADD NEW COMMAND")
    print("-"*30)
    cmd = input("Enter command: ").strip()
    
    if cmd:
        commands = load_commands()
        commands.append(cmd)
        save_commands(commands)
        print(f"\n✅ Command added successfully! (#{len(commands)})")
    else:
        print("\n❌ No command entered!")
    
    input("\nPress Enter to continue...")

def remove_command_interactive():
    """Interactive command removal"""
    commands = load_commands()
    
    if not commands:
        print("\n📝 No commands to remove!")
        input("\nPress Enter to continue...")
        return
    
    print("\n🗑️ REMOVE COMMAND")
    print("-"*30)
    for i, cmd in enumerate(commands, 1):
        print(f"  {i}. {cmd}")
    
    try:
        choice = input("\nEnter command number to remove (0 to cancel): ").strip()
        if choice == '0':
            return
        
        index = int(choice)
        if 1 <= index <= len(commands):
            removed = commands.pop(index - 1)
            save_commands(commands)
            print(f"\n✅ Command removed: {removed}")
        else:
            print("\n❌ Invalid command number!")
    except ValueError:
        print("\n❌ Please enter a valid number!")
    
    input("\nPress Enter to continue...")

def run_command_interactive(num):
    """Run selected command"""
    commands = load_commands()
    
    if not commands:
        print("\n📝 No commands to run!")
        input("\nPress Enter to continue...")
        return False
    
    if 1 <= num <= len(commands):
        cmd = commands[num - 1]
        clear_screen()
        print(f"🚀 Running command #{num}: {cmd}")
        print("="*50)
        print("\n" + "-"*50)
        print("COMMAND OUTPUT:")
        print("-"*50)
        
        # Run the command
        result = os.system(cmd)
        
        print("\n" + "-"*50)
        print(f"✅ Command finished with code: {result}")
        print("-"*50)
        
        input("\nPress Enter to return to menu...")
        return True
    else:
        print(f"\n❌ Invalid command number! (1-{len(commands)})")
        input("\nPress Enter to continue...")
        return False

def main():
    """Main interactive loop"""
    while True:
        show_menu()
        commands = load_commands()
        
        choice = input("\nYour choice: ").strip().upper()
        
        if choice == 'Q':
            print("\n👋 Goodbye!")
            break
        
        elif choice == 'A':
            add_command_interactive()
        
        elif choice == 'R':
            remove_command_interactive()
        
        elif choice == 'L':
            input("\nPress Enter to continue...")
        
        elif choice.isdigit():
            num = int(choice)
            run_command_interactive(num)
        
        else:
            print("\n❌ Invalid choice!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
