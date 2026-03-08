# Commerce: The Auction Engineering Platform

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

##  Overview
**Commerce** is a sophisticated full-stack auction engine meticulously engineered with **Django**. It is designed to handle the complex lifecycle of online bidding—from dynamic item listing to secure winner determination. This project highlights my focus on **Relational Database Design**, **Server-Side Validation**, and **Clean Architecture**.

---

##  Key Engineering Features

| Feature | Technical Implementation | Goal |
| :--- | :--- | :--- |
| **Active Auctions** | Dynamic querying of relational models. | Real-time Visibility |
| **Bidding Engine** | Comparative logic to ensure price increments. | Data Integrity |
| **User Watchlist** | Many-to-Many relationship mapping. | UX Personalization |
| **Auction Closure** | State-management for identifying & notifying winners. | Workflow Automation |
| **Interaction Layer** | Comment systems linked via Foreign Keys. | Community Engagement |

---

##  Technical Deep Dive

###  Architecture & Schema Design
The core of this platform is a robust **Relational Database Schema**. I engineered four interconnected models to ensure a seamless flow of data:
*   **User Model:** Manages secure authentication and personalized dashboards.
*   **Listing Model:** The central entity containing item metadata, categories, and status.
*   **Bid Model:** Tracks historical increments while enforcing strict value constraints.
*   **Comment Model:** Facilitates multi-user interaction through relational mapping.

###  Logic & Security
To ensure a fair and reliable auction environment, I implemented:
- **Server-Side Bid Validation:** Prevents bids that do not exceed the current highest offer.
- **Conditional Rendering:** The UI adapts dynamically based on user state (e.g., Auction Owner vs. Potential Bidder).
- **Access Control:** Enforced permission checks to ensure only authorized users can modify listing states.

###  UI/UX Philosophy
Applying **Human-Computer Interaction (HCI)** principles:
- **Responsive Layouts:** Built with Bootstrap for a mobile-first experience.
- **Visual Feedback:** Clear success/error messaging for bid submissions and auction results.

---

##  Installation
1. Clone the repo: `git clone https://github.com/TahaniAlsmari/commerce.git`
2. Install Django: `pip install django`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`
