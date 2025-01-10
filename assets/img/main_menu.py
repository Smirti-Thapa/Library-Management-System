import mysql.connector
from datetime import datetime
import os
import add_book
import add_member
import issue_book
import update_book
import return_book
import search_menu
import special_menu
import report_menu

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Update Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Issued Books")
        print("7. Search Books")
        print("8. Reports")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book.addition_book()
        elif choice == "2":
            add_member.addition_member()
        elif choice == "3":
            update_book.update_book()
        elif choice == "4":
            issue_book.issue_book()
        elif choice == "5":
            return_book.return_book()
        elif choice == "6":
            search_menu.menu_search()
        elif choice == "7":
            report_menu.report_menu()
        elif choice == "8":
            special_menu.special_menu()
        elif choice == "9":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
