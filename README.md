# Cartify
The Cartify Ecommerce Application is built using React for the front-end, Django for the back-end/REST API (https://cartify.up.railway.app/api/schema/docs/), and PostgreSQL for the database. The app allows users to browse products, add them to a cart, and complete transactions securely. It includes features like user authentication, order management, and product reviews.
# Cartify - Full Stack E-commerce Application

Cartify is a full-stack e-commerce application developed using Django, Django REST, React, React-Redux, AWS S3 Bucket, PostgreSQL, and Axios. It provides a comprehensive platform for building and managing online stores with features such as product listing, shopping cart functionality, user authentication, and order processing.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

## Features

Cartify comes with a range of powerful features to support your e-commerce store:

- **Product Listing:** Display products with details such as name, description, price, and image.
- **Product Filtering and Sorting:** Filter products based on categories, price range, and sorting options.
- **Shopping Cart:** Add products to a cart, modify quantities, and remove items.
- **User Authentication:** Allow users to sign up, log in, and manage their accounts.
- **Order Processing:** Process orders, calculate totals, and generate invoices.
- **AWS S3 Integration:** Store product images and other static assets in an AWS S3 Bucket for scalability and performance.
- **PostgreSQL Database:** Utilize a robust PostgreSQL database for data storage and retrieval.
- **API Communication:** Communicate with the backend API using Axios to perform CRUD operations on products, carts, and orders.
- **Responsive UI:** Build a responsive user interface using React and React-Redux for an optimal shopping experience.
- **AWS RDS:** Utilize Amazon RDS as the managed PostgreSQL database for secure and scalable data storage.
- **JWT Token Authentication:** Implement JSON Web Token (JWT) authentication using Django REST Framework for secure user authorization and access control.

## Technologies Used

Cartify is built using the following technologies:

- **Django:** A powerful Python web framework for building the backend API and handling server-side logic.
- **Django REST Framework:** A toolkit for building RESTful APIs with Django, used to create API endpoints for product, cart, and order management.
- **React:** A popular JavaScript library for building user interfaces, used to create the frontend views and components.
- **React-Redux:** A library that integrates React with Redux, a predictable state container for managing the application's global state.
- **AWS S3 Bucket:** Amazon Simple Storage Service is used to store static assets, including product images.
- **PostgreSQL:** A powerful open-source relational database management system used for data storage and retrieval.
- **Axios:** A popular JavaScript library for making HTTP requests, used to communicate with the backend API.

## Installation

To install and set up Cartify on your local machine, follow these steps:

1. Clone the Cartify repository from GitHub:

   ```shell
   git clone https://github.com/ifecog/Cartify.git
   ```

2. Navigate to the project's root directory:

   ```shell
   cd Cartify
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

   - On Windows:

     ```shell
     .\venv\Scripts\activate
     ```

5. Install the Python dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Install the JavaScript dependencies:

   ```shell
   npm install
   ```
   ```shell
   npx create-react-app react-app
   ```

7. Create a `.env` file in the project's root directory and provide the necessary environment variables. The required variables include database settings, AWS S3 credentials, and secret keys.

8. Set up the PostgreSQL database by running the following commands:

   ```shell
   python manage.py migrate
   python manage

.py createsuperuser
   ```

9. Start the development server:

   ```shell
   python manage.py runserver
   ```

10. Open a new terminal tab or window, navigate to the project's root directory, and start the frontend development server:

    ```shell
    npm start
    ```

You should now be able to access Cartify by visiting `http://localhost:3000` in your web browser.

## Usage

Once Cartify is set up and running, you can use the following steps to interact with the application:

1. Register a new user account or log in using existing credentials.
2. Browse the product listings and use the filters and sorting options to find desired products.
3. Add products to the shopping cart and modify quantities if needed.
4. Proceed to the checkout process and enter shipping and payment details.
5. Confirm the order and receive an order confirmation with an invoice.
6. As an admin, you can manage products, categories, and orders through the admin interface at `http://localhost:8000/admin`.

## Deployment

To deploy Cartify to a production environment, follow these steps:

1. Set up a production-ready database such as Amazon RDS or a managed PostgreSQL service.
2. Configure your production environment variables, including database settings, AWS S3 credentials, and secret keys.
3. Modify the Django settings file to use the appropriate production settings.
4. Set up a production-ready web server such as Nginx or Apache to serve the Django application.
5. Build the React frontend for production using the appropriate build commands.
6. Serve the built React frontend using the web server alongside the Django application.
7. Set up any necessary SSL certificates or security measures for secure communication.
8. Monitor the application for any errors or performance issues in the production environment.

## Contributing

Contributions to Cartify are welcome and encouraged! If you have any bug reports, feature requests, or improvements, please submit them as issues or pull requests on the GitHub repository.

## License

Cartify is licensed under the [MIT License](https://github.com/ifecog/Cartify/blob/main/LICENSE). You are free to use, modify, and distribute the application for personal or commercial purposes.
