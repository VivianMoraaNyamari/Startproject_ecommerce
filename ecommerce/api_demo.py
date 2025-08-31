import os
import sys
import django
from django.test import Client
from django.conf import settings

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

def demo_api():
    """
    Demo script for testing the e-commerce API endpoints using Django test client
    """
    client = Client()
    
    print("=" * 60)
    print("        E-COMMERCE API DEMONSTRATION")
    print("=" * 60)
    print()
    
    # 1. User Registration
    print("1. 📝 USER REGISTRATION")
    print("   Endpoint: POST /api/auth/register/")
    print("   Purpose: Create a new user account")
    print()
    
    registration_data = {
        "username": "demo_user",
        "email": "demo@example.com",
        "password": "demopassword123",
        "password_confirmation": "demopassword123",
        "first_name": "Demo",
        "last_name": "User",
        "phone_number": "+1234567890"
    }
    
    response = client.post('/api/auth/register/', registration_data, content_type='application/json')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 201:
        print("   ✅ Registration successful!")
        user_data = response.json()
        print(f"   User created: {user_data['user']['username']}")
        print(f"   Email: {user_data['user']['email']}")
    else:
        print(f"   ❌ Registration failed: {response.content.decode()}")
    
    print()
    
    # 2. User Login
    print("2. 🔐 USER LOGIN")
    print("   Endpoint: POST /api/auth/login/")
    print("   Purpose: Authenticate user and obtain token")
    print()
    
    login_data = {
        "username": "demo_user",
        "password": "demopassword123"
    }
    
    response = client.post('/api/auth/login/', login_data, content_type='application/json')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("   ✅ Login successful!")
        login_response = response.json()
        token = login_response.get('token')
        print(f"   Token received: {token[:20]}...")  # Show first 20 chars of token
    else:
        print(f"   ❌ Login failed: {response.content.decode()}")
        return
    
    print()
    
    # 3. Get Products (Unauthenticated)
    print("3. 🛍️ GET PRODUCTS (Public Access)")
    print("   Endpoint: GET /api/products/")
    print("   Purpose: Retrieve all available products")
    print()
    
    response = client.get('/api/products/')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        products = response.json()
        print(f"   ✅ Found {len(products)} products")
        
        if len(products) > 0:
            print("\n   Sample Products:")
            for i, product in enumerate(products[:3]):  # Show first 3 products
                print(f"   {i+1}. {product['name']} - ${product['price']}")
        else:
            print("   ℹ️ No products found. Add some products via admin first.")
    
    print()
    
    # 4. Get User Profile (Authenticated)
    print("4. 👤 USER PROFILE (Authenticated)")
    print("   Endpoint: GET /api/auth/profile/")
    print("   Purpose: Get authenticated user's profile data")
    print()
    
    # Set authorization header for authenticated request
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {token}'
    
    response = client.get('/api/auth/profile/')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        profile_data = response.json()
        print("   ✅ Profile retrieved successfully!")
        print(f"   Username: {profile_data['username']}")
        print(f"   Email: {profile_data['email']}")
        print(f"   Name: {profile_data['first_name']} {profile_data['last_name']}")
    else:
        print(f"   ❌ Profile access failed: {response.content.decode()}")
    
    print()
    
    # 5. Get Categories
    print("5. 📂 GET CATEGORIES")
    print("   Endpoint: GET /api/products/categories/")
    print("   Purpose: Retrieve all product categories")
    print()
    
    response = client.get('/api/products/categories/')
    print(f"   Status Code: {response.status_code}")
    
    if response.status_code == 200:
        categories = response.json()
        print(f"   ✅ Found {len(categories)} categories")
        
        if len(categories) > 0:
            print("\n   Categories:")
            for category in categories:
                print(f"   - {category['name']}")
    
    print()
    print("=" * 60)
    print("        DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    demo_api()
    