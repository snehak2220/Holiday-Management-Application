
# 🎉 Holiday Management Application  

A Django-based application that integrates with the Calendarific API to help users search and manage holidays by country, date, and type. It includes advanced features like search and filter options, holiday details modal, and pagination.  

---

## 🌟 Features  
- Search holidays by:
  - Country
  - Month
  - Year
  - Type
- Filter holidays by date range.  
- View detailed holiday information in a modal.  
- Pagination for easy navigation.  
- Responsive frontend using Bootstrap.  

---

## Technologies Used
- **Backend:**
  - Django (Python)
  - Django Rest Framework
- **Frontend:**
  - HTML, CSS, Bootstrap, JavaScript
- **API Integration:**
  - [Calendarific API](https://calendarific.com/)

---

## Prerequisites
- Python (>= 3.6)
- Django (>= 4.0)
- djangorestframework
- dotenv
- requests
- Git
- Calendarific API Key (Create an account at [Calendarific](https://calendarific.com/) to obtain one)

---

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/snehak2220/HolidaysApp.git
    cd HolidaysApp
    ```
    
2. **Install The Requirements:**
    ```sh
    pip install -r requirements.txt
    ```
3. **Setup API Key:**
   ```sh
   CALENDARIFIC_API_KEY=your_api_key_here
    ```
4. **Apply Migrations:**
   ```sh
    python manage.py migrate
   ```
5. **Run The Application:**
    ```sh
    python manage.py runserver
    ```
## 🚀 Usage
  - Select the country, year, month, and type to search for holidays.
  - Use the date filter to narrow down holiday results.
  - Click on "Details" to view more information about the holiday.  

----
## 🔗 API Endpoints
 /api/holidays/ - List holidays with filters:
- country: ISO 3166-1 alpha-2 code (e.g., US, IN)
- year: Year (e.g., 2025)
- month: Month (e.g., 1 for January)
- type: Holiday type (e.g., national, religious)
- date: Specific date (e.g., 2025-01-01)

---
## 🛠️ Built With
- Django - Backend framework
- Django REST Framework - API implementation
- Calendarific API - Holiday data provider
- Bootstrap - Responsive frontend
- JavaScript - Dynamic interactivity

---
## 🤝 Contributing
Contributions are welcome!

- Fork the repository.
- Create a new branch (feature/new-feature).
- Make your changes and commit (git commit -m "Add new feature").
- Push to the branch (git push origin feature/new-feature).
- Open a Pull Request.

---
## 📝 License
This project is licensed under the MIT License.

---
## 📞 Contact
For any questions or feedback, feel free to reach out:

- GitHub: snehak2220
