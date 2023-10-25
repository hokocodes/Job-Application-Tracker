import xml.etree.ElementTree as ET
from datetime import date

class JobApplicationTracker:
    def __init__(self):
        self.tree = ET.ElementTree()
        self.root = None
        self.load_applications()

    def load_applications(self):
        try:
            self.tree = ET.parse("job_applications.xml")
            self.root = self.tree.getroot()
        except FileNotFoundError:
            self.root = ET.Element("jobApplications")

    def save_applications(self):
        self.tree = ET.ElementTree(self.root)
        self.tree.write("job_applications.xml")

    def display_applications(self):
        for application in self.root.findall("application"):
            applicant = application.find("applicant")
            applicant_name = f"{applicant.find('name/first').text} {applicant.find('name/last').text}"
            position = application.find("position/title").text
            company = application.find("position/company").text
            status = application.find("applicationStatus/status").text
            date_submitted = application.find("applicationStatus/date").text

            print(f"Applicant: {applicant_name}, Position: {position}, "
                  f"Company: {company}, Status: {status}, Date Submitted: {date_submitted}")

    def add_application(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")

        title = input("Enter the position title: ")
        company = input("Enter the company name: ")
        location = input("Enter the job location: ")

        status = "Submitted"
        date_submitted = str(date.today())

        new_application = ET.SubElement(self.root, "application")
        applicant = ET.SubElement(new_application, "applicant")
        ET.SubElement(applicant, "name").extend([ET.Element("first").text(first_name), ET.Element("last").text(last_name)])
        ET.SubElement(applicant, "contact").extend([ET.Element("email").text(email), ET.Element("phone").text(phone)])

        position = ET.SubElement(new_application, "position")
        ET.SubElement(position, "title").text = title
        ET.SubElement(position, "company").text = company
        ET.SubElement(position, "location").text = location

        application_status = ET.SubElement(new_application, "applicationStatus")
        ET.SubElement(application_status, "status").text = status
        ET.SubElement(application_status, "date").text = date_submitted

        print("Application added successfully!")

    def run(self):
        while True:
            print("\nJob Application Tracker Menu:")
            print("1. View Applications")
            print("2. Add Application")
            print("3. Save and Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                self.display_applications()
            elif choice == "2":
                self.add_application()
            elif choice == "3":
                self.save_applications()
                print("Applications saved. Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    app = JobApplicationTracker()
    app.run()
