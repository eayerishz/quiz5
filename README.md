## Project Overview

This project involves building a full-stack web application with a focus on creating both frontend and backend systems. The backend will manage user and product data, while the frontend will present the data in an interactive way for users. You will be working as a pair—one will handle the **Frontend** and the other will handle the **Backend**.

## Backend Instructions

### Models

1. **Accounts:**
   - Use the built-in user model (e.g., Django’s `User` model or another framework's equivalent).
   - DjangoAdmin (username: quiz ; password: 123)
   
2. **Products:**
   - The Product model should have the following fields:
     - `user` (ForeignKey or similar linking to the user model)
     - `name` (string)
     - `image` (image URL or file path)
     - `brand` (string)
     - `category` (string)
     - `description` (text)
     - `rating` (float)
     - `numReviews` (integer)
     - `price` (decimal or float)
     - `stock` (integer)
     - `createdAt` (datetime)
     - `updatedAt` (datetime)
     - `uuid` (UUID field)

### Views

1. **Accounts Views:**
   - `get_users()` - Returns a list of all users.
   - `get_user()` - Returns detailed information of a single user.
   
2. **Products Views:**
   - `get_products()` - Returns a list of all products.
   - `get_product()` - Returns detailed information for a specific product.

### Requirements

1. Create a GitHub repository to store both the **Frontend** and **Backend** projects.
2. Your project must include the following files:
   - `.gitignore` - To ignore unnecessary files and folders.
   - `README.md` - This file.
   - `requirements.txt` - List of required dependencies.
   
3. Ensure the **README** file is complete and accurate. If there is a step missing to run the project, it will not be fixed.

---

## Frontend Instructions

### Screens

1. **Dashboard Screen (`Dashboard.jsx`)**
   - List both products and users:
     - **Products:** Display them as Cards.
     - **Users:** Display them as a Table.

2. **Product Screen (`ProductScreen.jsx`)**
   - Display detailed information for a specific product.

3. **User Screen (`UserScreen.jsx`)**
   - Display detailed information for a specific user.

### Components

1. **Card Component (`Card.jsx`)**
   - Display product information such as name, image, description, rating, price, and a CTA button for redirecting.

2. **Navbar Component (`Navbar.jsx`)**
   - Display the main navigation.

3. **Table Component (`Table.jsx`)**
   - Display user information in a table format, including:
     - ID
     - Username
     - `is_admin`, `is_staff`, and `is_active`
     - CTA Button for redirecting

4. **Rating Component (`Rating.jsx`)**
   - Display a star rating for products using FontAwesome.

### Dashboard

- List products as cards with the following details:
  - Name
  - Image
  - Truncated description
  - Star rating (FontAwesome)
  - Price
  - CTA button for redirecting to product details.

- List users as a table with:
  - ID
  - Username
  - `is_admin`, `is_staff`, and `is_active`
  - CTA button for redirecting to the user details page.

### Backend Connection

- Use **Axios** to connect the frontend to the backend and retrieve the data (products and users).
  
---

## Setup and Installation

1. Clone the GitHub repository for both Frontend and Backend projects.

2. **Backend Setup:**
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Frontend Setup:**
   - Install the required dependencies by running:
     ```bash
     npm install
     ```

4. **Run Backend:**
   - Ensure that the backend API is running locally or on a server.
   - You can start the backend server using:
     ```bash
     python manage.py runserver
     ```

5. **Run Frontend:**
   - Start the frontend project:
     ```bash
     npm start
     ```
