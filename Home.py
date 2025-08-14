<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bug Palace - Hüllőkellékek, Táplálék, Állatok - Mind Egy Helyen</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #f8f9fa;
        }

        /* Header */
        .header {
            background: linear-gradient(135deg, #1e3d59 0%, #2c3e50 100%);
            color: white;
            padding: 15px 0;
            position: fixed;
            width: 100%;
            top: 29px;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .header-top {
            background: #16a085;
            text-align: center;
            padding: 8px 0;
            font-size: 14px;
            font-weight: 600;
        }

        .header-main {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

        .logo-container {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo {
            height: 60px;
            width: auto;
        }

        .brand-name {
            font-size: 28px;
            font-weight: bold;
            color: #27ae60;
        }

        .nav-menu {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        .nav-menu a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 10px 15px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        .nav-menu a:hover {
            background: #27ae60;
            transform: translateY(-2px);
        }

        .cart-icon {
            position: relative;
            background: #e67e22;
            padding: 12px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .cart-icon:hover {
            background: #d35400;
            transform: scale(1.1);
        }

        .cart-count {
            position: absolute;
            top: -5px;
            right: -5px;
            background: #e74c3c;
            color: white;
            border-radius: 50%;
            width: 25px;
            height: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #2c3e50 0%, #1e3d59 100%);
            color: white;
            padding: 80px 0 80px;
            text-align: center;
            margin-top: 104px;
        }

        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .social-proof-badge {
            background: #27ae60;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 10px 20px;
            border-radius: 50px;
            margin-bottom: 30px;
            font-weight: 600;
        }

        .stars {
            color: #f1c40f;
            font-size: 18px;
        }

        .hero-headline {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-subheadline {
            font-size: 20px;
            margin-bottom: 20px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            opacity: 0.9;
            line-height: 1.5;
        }

        .hero-cta {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 18px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            margin-top: 10px;
        }

        .hero-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .hero-image {
            margin-top: 50px;
            max-width: 600px;
            width: 100%;
            height: 400px;
            background: #34495e;
            border-radius: 20px;
            margin-left: auto;
            margin-right: auto;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #bdc3c7;
            font-size: 18px;
        }

        /* Pain Point Section */
        .pain-point-section {
            background: #f8f9fa;
            padding: 80px 0;
        }

        .pain-point-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .pain-point-content {
            padding: 20px 0;
        }

        .pain-point-title {
            font-size: 42px;
            font-weight: bold;
            color: #2c3e50;
            line-height: 1.2;
            margin-bottom: 25px;
        }

        .pain-point-description {
            font-size: 18px;
            color: #5a6c7d;
            line-height: 1.6;
            margin-bottom: 35px;
        }

        .pain-point-cta {
            background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%);
            color: white;
            padding: 18px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .pain-point-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .pain-point-image {
            width: 100%;
            height: 400px;
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 18px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* Price Comparison Section */
        .price-comparison {
            background: white;
            padding: 80px 0;
        }

        .comparison-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        .comparison-card {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .comparison-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .competitor-card {
            border: 2px solid #e74c3c;
        }

        .our-card {
            border: 2px solid #27ae60;
            background: linear-gradient(135deg, #e8f5e8 0%, #f8f9fa 100%);
        }

        .comparison-header {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #ecf0f1;
        }

        .competitor-header {
            color: #e74c3c;
        }

        .our-header {
            color: #27ae60;
        }

        .price-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            padding: 10px 0;
            border-bottom: 1px solid #ecf0f1;
        }

        .price-label {
            font-weight: 500;
        }

        .price-value {
            font-weight: bold;
        }

        .competitor-price {
            color: #e74c3c;
        }

        .our-price {
            color: #27ae60;
        }

        .total-savings {
            background: #27ae60;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            font-weight: bold;
            font-size: 18px;
        }

        /* Premium Product Highlight */
        .premium-highlight {
            background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%);
            color: white;
            padding: 60px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .premium-highlight::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="stars" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23stars)"/></svg>');
            opacity: 0.3;
        }

        .premium-content {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .premium-products-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-top: 30px;
        }

        .premium-badge {
            background: #f1c40f;
            color: #2c3e50;
            padding: 8px 20px;
            border-radius: 25px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 20px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .premium-title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .premium-subtitle {
            font-size: 18px;
            opacity: 0.9;
            margin-bottom: 30px;
        }

        .premium-product-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .premium-product-image {
            width: 300px;
            height: 250px;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            margin: 0 auto 25px;
            overflow: hidden;
        }

        .premium-product-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .premium-product-description {
            font-size: 16px;
            margin-bottom: 20px;
            opacity: 0.9;
        }

        .premium-price {
            font-size: 42px;
            font-weight: bold;
            color: #f1c40f;
            margin-bottom: 20px;
        }

        .premium-cta {
            background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
            color: #2c3e50;
            padding: 18px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }

        .premium-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }

        .starter-package-card {
            background: linear-gradient(135deg, #27ae60 0%, #16a085 100%);
            border: 2px solid rgba(255,255,255,0.2);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            color: white;
        }

        .starter-badge {
            background: #f1c40f;
            color: #2c3e50;
            padding: 8px 20px;
            border-radius: 25px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 20px;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .starter-product-image {
            width: 300px;
            height: 200px;
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            margin: 0 auto 25px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 14px;
            text-align: center;
        }

        .starter-product-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .starter-price {
            font-size: 36px;
            font-weight: bold;
            color: #f1c40f;
            margin-bottom: 20px;
        }

        .starter-cta {
            background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
            color: #2c3e50;
            padding: 18px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            width: 100%;
        }

        .starter-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }

        /* How It Works Section */
        .how-it-works {
            background: white;
            padding: 80px 0;
        }

        .steps-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            margin-top: 50px;
        }

        .step-card {
            background: #f8f9fa;
            border: 2px solid #ecf0f1;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
        }

        .step-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-color: #27ae60;
        }

        .step-image {
            width: 100%;
            height: 120px;
            border-radius: 10px;
            margin-bottom: 20px;
            overflow: hidden;
        }

        .step-number {
            background: linear-gradient(135deg, #27ae60 0%, #16a085 100%);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
            margin: 0 auto 20px;
            position: relative;
            z-index: 2;
        }

        .step-title {
            font-size: 22px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 15px;
        }

        .step-description {
            color: #7f8c8d;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .step-features {
            background: #e8f5e8;
            border-radius: 8px;
            padding: 15px;
            font-size: 14px;
            color: #27ae60;
        }

        .product-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 11px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .badge-new {
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
        }

        .badge-popular {
            background: linear-gradient(135deg, #f1c40f 0%, #f39c12 100%);
            color: #2c3e50;
        }

        .badge-hot {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
        }
        .social-proof {
            background: white;
            padding: 80px 0;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .section-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 50px;
            color: #2c3e50;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 60px;
        }

        .testimonial {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            border-left: 5px solid #27ae60;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .testimonial-text {
            font-size: 16px;
            margin-bottom: 20px;
            font-style: italic;
            line-height: 1.6;
        }

        .testimonial-author {
            font-weight: bold;
            color: #27ae60;
        }

        /* Product Benefits */
        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        .benefit-item {
            text-align: center;
            padding: 30px 20px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .benefit-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .benefit-icon {
            width: 80px;
            height: 80px;
            background: #27ae60;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            color: white;
        }

        .benefit-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .benefit-description {
            font-size: 14px;
            color: #7f8c8d;
            line-height: 1.5;
        }

        /* Bestselling Products */
        .bestselling {
            background: #ecf0f1;
            padding: 80px 0;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }

        /* Product Categories Filter */
        .category-filter {
            text-align: center;
            margin-bottom: 40px;
        }

        .filter-buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .filter-btn {
            background: #ecf0f1;
            color: #2c3e50;
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .filter-btn.active,
        .filter-btn:hover {
            background: #27ae60;
            color: white;
        }

        .product-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            opacity: 1;
            position: relative;
        }

        .product-card.hidden {
            display: none;
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .product-image {
            width: 100%;
            height: 200px;
            background: #34495e;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #bdc3c7;
            font-size: 16px;
            position: relative;
        }

        .product-info {
            padding: 20px;
        }

        .product-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .product-rating {
            color: #f1c40f;
            margin-bottom: 10px;
        }

        .product-description {
            font-size: 14px;
            color: #7f8c8d;
            margin-bottom: 15px;
            line-height: 1.5;
        }

        .product-price {
            font-size: 20px;
            font-weight: bold;
            color: #27ae60;
            margin-bottom: 15px;
        }

        .add-to-cart {
            background: #e67e22;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            width: 100%;
            transition: all 0.3s ease;
            margin-bottom: 10px;
        }

        .friction-reducer {
            font-size: 11px;
            color: #27ae60;
            text-align: center;
            margin: 0;
            line-height: 1.3;
        }

        .add-to-cart:hover {
            background: #d35400;
        }

        /* Comparison Table */
        .comparison-table {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin-top: 50px;
        }

        .comparison-table table {
            width: 100%;
            border-collapse: collapse;
        }

        .comparison-table th {
            padding: 20px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
        }

        .comparison-table th:first-child {
            background: #34495e;
            color: white;
            text-align: left;
        }

        .comparison-table th:nth-child(2) {
            background: #e74c3c;
            color: white;
        }

        .comparison-table th:last-child {
            background: #27ae60;
            color: white;
        }

        .comparison-table td {
            padding: 15px 20px;
            border-bottom: 1px solid #ecf0f1;
            vertical-align: middle;
        }

        .comparison-table td:first-child {
            font-weight: 600;
            background: #f8f9fa;
            color: #2c3e50;
        }

        .comparison-table td:nth-child(2) {
            text-align: center;
            color: #e74c3c;
        }

        .comparison-table td:last-child {
            text-align: center;
            color: #27ae60;
        }

        .comparison-icon {
            font-size: 24px;
            margin-right: 10px;
        }

        /* Top Newsletter Banner */
        .top-newsletter-banner {
            background: linear-gradient(135deg, #27ae60 0%, #16a085 100%);
            color: white;
            text-align: center;
            padding: 8px 0;
            font-size: 13px;
            font-weight: 600;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1001;
            animation: pulse 3s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        /* Email Input for Lead Magnet */
        .cta-form {
            max-width: 500px;
            margin: 40px auto 0;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .email-input {
            flex: 1;
            min-width: 250px;
            padding: 15px 20px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
        }

        .email-submit {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 15px 30px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .email-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        /* Customer Photos Carousel - Above the Fold */
        .customer-photos-hero {
            background: rgba(255,255,255,0.05);
            padding: 10px 0;
            overflow: hidden;
            margin-bottom: 10px;
        }

        .photos-carousel {
            display: flex;
            animation: scroll 25s linear infinite;
            gap: 15px;
        }

        .customer-photo {
            min-width: 200px;
            height: 150px;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            flex-shrink: 0;
        }

        .customer-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .photo-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.8));
            color: white;
            padding: 10px;
            font-size: 12px;
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        .photos-carousel:hover {
            animation-play-state: paused;
        }

        /* Hero CTA with Email */
        .hero-cta-section {
            margin-top: 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-form {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .hero-email-input {
            flex: 1;
            min-width: 250px;
            padding: 15px 20px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
        }

        .hero-email-submit {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 15px 30px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            white-space: nowrap;
        }

        .hero-email-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .cta-section {
            background: linear-gradient(135deg, #1e3d59 0%, #2c3e50 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }

        .cta-title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .cta-description {
            font-size: 18px;
            margin-bottom: 40px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            opacity: 0.9;
        }

        .cta-button {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 20px 50px;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        /* Subscription Value Props */
        .subscription-benefits {
            background: white;
            padding: 80px 0;
        }

        .benefits-two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-top: 50px;
            align-items: center;
        }

        .benefit-accordion {
            background: #f8f9fa;
            border-radius: 15px;
            overflow: hidden;
            margin-bottom: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .benefit-header {
            background: #27ae60;
            color: white;
            padding: 20px;
            cursor: pointer;
            font-weight: bold;
            font-size: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .benefit-header:hover {
            background: #229954;
        }

        .benefit-content {
            padding: 0 20px;
            max-height: 0;
            overflow: hidden;
            transition: all 0.3s ease;
            background: white;
        }

        .benefit-content.active {
            max-height: 200px;
            padding: 20px;
        }

        .subscription-image {
            width: 100%;
            height: 400px;
            background: #f8f9fa;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: #7f8c8d;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .savings-highlight {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 15px 25px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 18px;
            text-align: center;
            margin: 20px 0;
            display: inline-block;
        }

        .final-closer {
            background: linear-gradient(135deg, #1e3d59 0%, #2c3e50 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .closer-background {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('pic18.webp') center/cover;
            opacity: 0.3;
            z-index: 0;
        }

        .closer-content {
            position: relative;
            z-index: 1;
            max-width: 800px;
            margin: 0 auto;
        }

        .closer-title {
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .closer-description {
            font-size: 20px;
            margin-bottom: 40px;
            opacity: 0.9;
            line-height: 1.5;
        }

        .closer-cta {
            background: linear-gradient(135deg, #e67e22 0%, #d35400 100%);
            color: white;
            padding: 20px 50px;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }

        .closer-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .footer {
            background: #2c3e50;
            color: white;
            padding: 50px 0 20px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            margin-bottom: 30px;
        }

        .footer-section h3 {
            font-size: 18px;
            margin-bottom: 20px;
            color: #27ae60;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            padding: 5px 0;
        }

        .footer-section ul li a {
            color: #bdc3c7;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-section ul li a:hover {
            color: #27ae60;
        }

        .footer-bottom {
            border-top: 1px solid #34495e;
            padding-top: 20px;
            text-align: center;
            color: #95a5a6;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-menu {
                display: none;
            }

            .hero-headline {
                font-size: 32px;
            }

            .hero-subheadline {
                font-size: 16px;
            }

            .comparison-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .header-main {
                flex-direction: column;
                gap: 20px;
            }

            .cta-form {
                flex-direction: column;
                align-items: center;
            }

            .email-input {
                min-width: 280px;
            }

            .customer-photo {
                min-width: 180px;
                height: 120px;
            }

            .hero-form {
                flex-direction: column;
                align-items: center;
            }

            .hero-email-input {
                min-width: 280px;
                margin-bottom: 10px;
            }

            .customer-photos-hero {
                padding: 8px 0;
                margin-bottom: 8px;
            }

            .closer-title {
                font-size: 28px;
            }

            .closer-description {
                font-size: 16px;
            }

            .filter-buttons {
                gap: 10px;
            }

            .filter-btn {
                padding: 8px 15px;
                font-size: 14px;
            }

            .comparison-table {
                overflow-x: auto;
            }

            .comparison-table th,
            .comparison-table td {
                padding: 10px;
                font-size: 14px;
            }

            .comparison-table th {
                font-size: 16px;
            }

            .faq-question {
                font-size: 16px;
            }

            .top-newsletter-banner {
                font-size: 11px;
                padding: 6px 0;
            }

            .benefits-two-column {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .benefit-header {
                font-size: 16px;
                padding: 15px;
            }

            .savings-highlight {
                font-size: 16px;
                padding: 12px 20px;
            }

            .premium-title {
                font-size: 28px;
            }

            .premium-product-card {
                padding: 30px 20px;
            }

            .premium-price {
                font-size: 32px;
            }

            .premium-products-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .starter-product-image {
                width: 250px;
                height: 180px;
            }

            .starter-price {
                font-size: 28px;
            }

            .pain-point-container {
                grid-template-columns: 1fr;
                gap: 40px;
            }

            .pain-point-title {
                font-size: 32px;
            }

            .pain-point-description {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <!-- Top Newsletter Banner -->
    <div class="top-newsletter-banner">
        🎉 HÍRLEVELÜNKRE FELIRATKOZVA 10% KEDVEZMÉNY az összes termékből! Iratkozz fel most! 📧
    </div>

    <!-- Header -->
    <header class="header">
        <div class="header-main">
            <div class="logo-container">
                <img src="pic19.webp" alt="Bug Palace Logo" class="logo">
            </div>
            
            <nav>
                <ul class="nav-menu">
                    <li><a href="#home">Főoldal</a></li>
                    <li><a href="#products">Termékek</a></li>
                    <li><a href="#about">Rólunk</a></li>
                    <li><a href="#contact">Kapcsolat</a></li>
                    <li><a href="aszf.html">ÁSZF</a></li>
                </ul>
            </nav>
            
            <div class="cart-icon">
                🛒
                <span class="cart-count">0</span>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-container">
            <!-- Customer Photos Carousel at Top -->
            <div class="customer-photos-hero">
                <div class="photos-carousel">
                    <div class="customer-photo">
                        <img src="pic2.webp" alt="Egészséges leopárdgekkó">
                        <div class="photo-overlay">
                            <strong>Péter gekkója</strong><br>
                            "Bug Palace táplálékkal"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic3.webp" alt="Gyönyörű terráriumbeállítás">
                        <div class="photo-overlay">
                            <strong>Andrea terráriuma</strong><br>
                            "Minden kellék tőlünk"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic4.webp" alt="Egészséges kaméleon">
                        <div class="photo-overlay">
                            <strong>Gábor kaméleonja</strong><br>
                            "Friss tücsökkel táplálva"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic5.webp" alt="Boldog hüllőtartó">
                        <div class="photo-overlay">
                            <strong>Máté gyűjteménye</strong><br>
                            "5 gekkó, mind egészséges"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic6.webp" alt="Terráriumban evés">
                        <div class="photo-overlay">
                            <strong>Kata hüllői</strong><br>
                            "Imádják a lisztkukacot"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic7.webp" alt="Egészséges iguana">
                        <div class="photo-overlay">
                            <strong>Zoli iguanája</strong><br>
                            "1 éve vásárló"
                        </div>
                    </div>
                    
                    <!-- Duplicate for seamless loop -->
                    <div class="customer-photo">
                        <img src="pic2.webp" alt="Egészséges leopárdgekkó">
                        <div class="photo-overlay">
                            <strong>Péter gekkója</strong><br>
                            "Bug Palace táplálékkal"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic3.webp" alt="Gyönyörű terráriumbeállítás">
                        <div class="photo-overlay">
                            <strong>Andrea terráriuma</strong><br>
                            "Minden kellék tőlünk"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic4.webp" alt="Egészséges kaméleon">
                        <div class="photo-overlay">
                            <strong>Gábor kaméleonja</strong><br>
                            "Friss tücsökkel táplálva"
                        </div>
                    </div>
                    
                    <div class="customer-photo">
                        <img src="pic5.webp" alt="Boldog hüllőtartó">
                        <div class="photo-overlay">
                            <strong>Máté gyűjteménye</strong><br>
                            "5 gekkó, mind egészséges"
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="social-proof-badge">
                <span class="stars">★★★★★</span>
                <span>1500+ 5 csillagos értékelés</span>
            </div>
            
            <h1 class="hero-headline">Egészséges Hüllők, Ingyenes Heti Táplálékszállítás</h1>
            
            <p class="hero-subheadline">
                Fáradt vagy a rossz tanácsoktól és a 4 különböző bolt végigjárásától? Nálunk minden hüllős termék egy helyen - táplálékától a terráriumig, szakértő csapattal aki tényleg ért a hüllőkhöz, nem csak árulja őket.
            </p>
            
            <p style="background: rgba(231, 126, 34, 0.1); padding: 15px; border-radius: 10px; margin: 20px auto; max-width: 600px; border-left: 4px solid #e67e22; font-size: 16px; font-weight: 500;">
                📸 <strong>Minden állat egyénileg fotózva!</strong> Pontosan azt kapod, amit a képen látsz - nincs meglepetés, nincs csalódás!
            </p>
            
            <div class="hero-cta-section">
                <a href="#products" class="hero-cta">TERMÉKEK MEGTEKINTÉSE</a>
                <p style="font-size: 12px; opacity: 0.7; margin: 15px 0 0 0; color: #27ae60; text-align: center;">
                    ✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia
                </p>
            </div>
            
            <div class="hero-image">
                <img src="pic1.webp" alt="Hüllő termékek" style="width:100%; height:100%; object-fit:cover; border-radius:20px;">
            </div>
        </div>
    </section>

    <!-- Pain Point + Price Comparison Section -->
    <section class="pain-point-section">
        <div class="container">
            <div class="pain-point-container">
                <div class="pain-point-content">
                    <h2 class="pain-point-title">Elég a Stresszes, Drága Hüllőtartásból és a Rossz Tanácsokból!</h2>
                    <p class="pain-point-description">
                        Fáradt vagy a 4 különböző bolt végigjárásától? A bizonytalan szállításoktól? A haldokló élő táplálékról? A félrevezető tanácsoktól kezdő eladóktól? 
                        <br><br>
                        <strong>Itt az ideje, hogy professzionális megoldásra váltsl:</strong> Minden egy helyen, szakértő csapattal, garantált minőségben, automatikus heti szállítással.
                    </p>
                    <a href="#premium-products" class="pain-point-cta">SZAKÉRTŐI MEGOLDÁSOK</a>
                </div>
                <div class="pain-point-image">
                    <img src="pic18.webp" alt="Problémák a hagyományos hüllőtartásban" style="width:100%; height:100%; object-fit:cover; border-radius:15px;">
                </div>
            </div>
            
            <!-- Price Comparison Cards -->
            <div class="comparison-grid" style="margin-top: 60px;">
                <div class="comparison-card competitor-card">
                    <h3 class="comparison-header competitor-header">🏪 Hagyományos Pet Shopok</h3>
                    <div class="price-item">
                        <span class="price-label">Heti táplálék</span>
                        <span class="price-value competitor-price">6.000 Ft</span>
                    </div>
                    <div class="price-item">
                        <span class="price-label">Szállítási díj</span>
                        <span class="price-value competitor-price">1.500 Ft</span>
                    </div>
                    <div class="price-item">
                        <span class="price-label"><strong>Heti összesen</strong></span>
                        <span class="price-value competitor-price"><strong>7.500 Ft</strong></span>
                    </div>
                    <div class="price-item">
                        <span class="price-label"><strong>Havi összesen</strong></span>
                        <span class="price-value competitor-price"><strong>30.000 Ft</strong></span>
                    </div>
                </div>

                <div class="comparison-card our-card">
                    <h3 class="comparison-header our-header">🏆 Bug Palace Előfizetés</h3>
                    <div class="price-item">
                        <span class="price-label">Heti táplálék</span>
                        <span class="price-value our-price">5.000 Ft</span>
                    </div>
                    <div class="price-item">
                        <span class="price-label">Szállítási díj</span>
                        <span class="price-value our-price">0 Ft</span>
                    </div>
                    <div class="price-item">
                        <span class="price-label"><strong>Heti összesen</strong></span>
                        <span class="price-value our-price"><strong>5.000 Ft</strong></span>
                    </div>
                    <div class="price-item">
                        <span class="price-label"><strong>Havi összesen</strong></span>
                        <span class="price-value our-price"><strong>20.000 Ft</strong></span>
                    </div>
                    <div class="total-savings">
                        💰 Havi 10.000 Ft megtakarítás!<br>
                        <small>Évi 120.000 Ft spórolás!</small>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works">
        <div class="container">
            <h2 class="section-title">Hogyan Működik? Egyszerű Mint 1-2-3</h2>
            <p style="text-align: center; font-size: 18px; color: #7f8c8d; max-width: 600px; margin: 0 auto;">
                Magas sikerességi arány és könnyű kezelhetőség - így jutunk el a stresszmentes hüllőtartáshoz!
            </p>
            
            <div class="steps-grid">
                <div class="step-card">
                    <div class="step-image">
                        <img src="pic3.webp" alt="Előfizetés beállítása" style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
                    </div>
                    <div class="step-number">1</div>
                    <h3 class="step-title">Előfizetés Beállítása</h3>
                    <p class="step-description">
                        Válaszd ki, milyen táplálékot szeretnél hetente vagy kéthetente. Állíts be mindent egyszer, aztán automatikus lesz!
                    </p>
                    <div class="step-features">
                        ✅ 1-2 hetente opció<br>
                        ✅ Bármikor módosítható<br>
                        ✅ Egyedi mennyiségek
                    </div>
                </div>

                <div class="step-card">
                    <div class="step-image">
                        <img src="pic6.webp" alt="Automatikus szállítás" style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
                    </div>
                    <div class="step-number">2</div>
                    <h3 class="step-title">Automatikus Szállítás</h3>
                    <p class="step-description">
                        Minden vasárnap automatikusan érkezik a friss táplálék. Soha nem kell emlékezned rendelésre!
                    </p>
                    <div class="step-features">
                        ✅ Vasárnapi szállítás<br>
                        ✅ 99% élő érkezési arány<br>
                        ✅ Ingyenes szállítás
                    </div>
                </div>

                <div class="step-card">
                    <div class="step-image">
                        <img src="pic7.webp" alt="Teljes rugalmasság" style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
                    </div>
                    <div class="step-number">3</div>
                    <h3 class="step-title">Teljes Rugalmasság</h3>
                    <p class="step-description">
                        2 alkalommal skippelhetsz a 8 hétből. Hétfő-szerda között jelezd, ha az adott héten nem kell szállítás!
                    </p>
                    <div class="step-features">
                        ✅ 2 skip / 8 hét<br>
                        ✅ Hétfő-szerda deadline<br>
                        ✅ VIP early access új termékekhez
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Premium Product Highlight Section -->
    <section class="premium-highlight" id="premium-products">
        <div class="premium-content">
            <div class="premium-badge">🏆 EXKLUZÍV KÍNÁLAT</div>
            <h2 class="premium-title">Prémium Ajánlatok Tapasztalt Hüllőtartóknak</h2>
            <p class="premium-subtitle">Válassz a csúcskategóriás állatjaink és a komplett kezdő csomagjaink közül</p>
            
            <div class="premium-products-grid">
                <!-- Prémium állat -->
                <div class="premium-product-card">
                    <div class="premium-product-image">
                        <img src="pic22.webp" alt="Albino Leopárdgekkó Pár" style="width:100%; height:100%; object-fit:cover; border-radius:15px;">
                    </div>
                    <h3 class="premium-product-title">🤍 Albino Leopárdgekkó Pár</h3>
                    <p class="premium-product-description">
                        <strong>📸 Egyénileg fotózva - pontosan ezt a párt kapod!</strong><br><br>
                        Ultra ritka albino génkombináció • Tenyészre kész • Igazolt származás • Generációkig tartó befektetés • 99.9% fehér szín purifikáció
                    </p>
                    <div class="premium-price">1.300.000 Ft</div>
                    <button class="premium-cta" onclick="handlePremiumPurchase()">EXKLUZÍV MEGRENDELÉS</button>
                    <p style="font-size: 12px; margin-top: 15px; opacity: 0.8;">
                        ⚡ Csak 1 pár elérhető • VIP szállítás • Személyes átadás lehetséges
                    </p>
                </div>

                <!-- Kezdő csomag -->
                <div class="starter-package-card">
                    <div class="starter-badge">🎯 KEZDŐ CSOMAG</div>
                    <div class="starter-product-image">
                        <img src="pic1.webp" alt="Teljes Leopárdgekkó Starter Csomag" style="width:100%; height:100%; object-fit:cover; border-radius:15px;">
                    </div>
                    <h3 class="starter-product-title">🦎 Teljes Leopárdgekkó Kezdő Csomag</h3>
                    <p style="font-size: 16px; margin-bottom: 20px; opacity: 0.9;">
                        <strong>Minden a sikeres kezdéshez egy csomagban!</strong><br><br>
                        ✅ 1 db egészséges leopárdgekkó (egyénileg fotózva)<br>
                        ✅ 60x40x40cm terrarium (felszerelve)<br>
                        ✅ Fűtés + UV világítás + termosztát<br>
                        ✅ Alom, búvóhelyek, itatótál<br>
                        ✅ <strong>3 hónapos táplálék előfizetés (ingyenes szállítás!)</strong><br>
                        ✅ Részletes gondozási útmutató<br>
                        ✅ 30 napos email támogatás
                    </p>
                    <div class="starter-price">189.000 Ft</div>
                    <p style="font-size: 14px; margin-bottom: 20px; opacity: 0.8;">
                        <s>Külön vásárolva: 245.000 Ft</s> • <strong>56.000 Ft megtakarítás!</strong>
                    </p>
                    <button class="starter-cta" onclick="handleStarterPurchase()">RENDELEM A CSOMAGOT</button>
                    <p style="font-size: 12px; margin-top: 15px; opacity: 0.8;">
                        🎁 Ajándék gondozási konzultáció • Azonnali kezdés • Sikeres első lépések
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Subscription Benefits -->
    <section class="subscription-benefits">
        <div class="container">
            <h2 class="section-title">Heti Előfizetés = Stresszmentes Hüllőtartás</h2>
            <p style="text-align: center; font-size: 18px; color: #7f8c8d; max-width: 600px; margin: 0 auto;">
                Csatlakozz a 3000+ hüllőtartóhoz akik már spórolnak időt, pénzt és idegeket az automatikus heti szállítással!
            </p>
            
            <div class="benefits-two-column">
            <div class="benefits-two-column">
                <div>
                    <div class="savings-highlight">
                        💰 Évi 104.000 Ft megtakarítás szállítási költségeken!
                    </div>
                    
                    <div class="benefit-accordion">
                        <div class="benefit-header" onclick="toggleBenefit(this)">
                            🚀 Automatikus Heti Szállítás
                            <span>+</span>
                        </div>
                        <div class="benefit-content">
                            <p><strong>Soha többé ne felejtsd el rendelni!</strong></p>
                            <p>Minden vasárnap automatikusan érkezik a friss táplálék az ajtód elé. Választhatsz heti vagy kéthetente szállítást is! Nem kell emlékezned, nem kell időt pocsékolnod rendeléssel.</p>
                        </div>
                    </div>

                    <div class="benefit-accordion">
                        <div class="benefit-header" onclick="toggleBenefit(this)">
                            💰 Hatalmas Megtakarítás 
                            <span>+</span>
                        </div>
                        <div class="benefit-content">
                            <p><strong>2000 Ft helyett 0 Ft szállítási költség hetente!</strong></p>
                            <p>Míg mások hetente 2000 Ft-ot fizetnek szállításért, te semmit. 8 hét alatt 16.000 Ft, egy év alatt 104.000 Ft megtakarítás! Ez több mint 2 havi táplálékra elég!</p>
                        </div>
                    </div>

                    <div class="benefit-accordion">
                        <div class="benefit-header" onclick="toggleBenefit(this)">
                            🎯 Mindig Friss Garantáltan
                            <span>+</span>
                        </div>
                        <div class="benefit-content">
                            <p><strong>Vasárnapi szállítás = maximális frissesség!</strong></p>
                            <p>A rovarok hétfő reggel érkeznek, amikor legfrissebbek. Nem hétvégén pusztulnak a raktárban, nem szerdán érkeznek félig döglötten. 99% élő érkezési arány!</p>
                        </div>
                    </div>

                    <div class="benefit-accordion">
                        <div class="benefit-header" onclick="toggleBenefit(this)">
                            🛡️ 8 Hetes Minimum Program
                            <span>+</span>
                        </div>
                        <div class="benefit-content">
                            <p><strong>8 hét garantált ellátás + teljes rugalmasság!</strong></p>
                            <p>Tudod hogy 8 hétig biztos lesz táplálék. 2 alkalommal skippelhetsz, ha útban vagy vagy más okból nincs szükség szállításra. Hétfő-szerda között jelezd! 8 hét után bármikor leállíthatod.</p>
                            <p style="background: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 15px; font-size: 13px; border-left: 4px solid #ffc107;"><strong>⚠️ Fontos:</strong> Az előfizetés bármikor megszakítható, de a már élvezett ingyenes szállításokat utólag felszámoljuk (2.000 Ft/alkalom).</p>
                        </div>
                    </div>
                </div>
                
                <div class="subscription-image">
                    <img src="pic17.webp" alt="Heti előfizetés előnyei" style="width:100%; height:100%; object-fit:cover; border-radius:15px;">
                </div>
            </div>
            
            <!-- VIP Membership Perks - külön szekció -->
            <div style="max-width: 800px; margin: 60px auto 0;">
                <div style="background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%); color: white; padding: 30px; border-radius: 15px; text-align: center;">
                    <h4 style="color: #f1c40f; font-size: 18px; margin-bottom: 20px;">🌟 VIP ELŐFIZETŐI ELŐNYÖK 🌟</h4>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; font-size: 14px;">
                        <div>🎂 <strong>Születésnapi ajándék</strong><br>Különleges meglepetés csomag</div>
                        <div>⚡ <strong>Early Access</strong><br>Új állatok 24 órával korábban</div>
                        <div>🎯 <strong>Exkluzív akciók</strong><br>Csak előfizetőknek kedvezmények</div>
                        <div>📞 <strong>Prioritásos support</strong><br>VIP ügyfélszolgálat</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Social Proof Section -->
    <section class="social-proof">
        <div class="container">
            <h2 class="section-title">Mit Mondanak Vásárlóink</h2>
            
            <div class="testimonials-grid">
                <div class="testimonial">
                    <p class="testimonial-text">"Végre egy webshop ahol minden van! A tücsök friss volt, a szállítás gyors, és a tanácsok profi szintűek. A gekkóm imádja az új táplálékot!"</p>
                    <div class="testimonial-author">- Kiss Péter, leopárdgekkó tartó</div>
                </div>
                
                <div class="testimonial">
                    <p class="testimonial-text">"15 éve tartok hüllőket, de ilyen minőségű rovarokat még nem kaptam. Minden él, friss, és pontosan időben érkezik. Ajánlom mindenkinek!"</p>
                    <div class="testimonial-author">- Nagy Andrea, terráriumtartó</div>
                </div>
                
                <div class="testimonial">
                    <p class="testimonial-text">"A tanácsaik alapján beállítottam a terráriumot és azóta sokkal egészségesebb a kaméleonom. Szakértelem és minőség egy helyen!"</p>
                    <div class="testimonial-author">- Szabó Gábor, kaméleon szakértő</div>
                </div>
            </div>

            <div class="benefits-grid">
                <div class="benefit-item">
                    <div class="benefit-icon">🌿</div>
                    <h3 class="benefit-title">Természetes Összetevők</h3>
                    <p class="benefit-description">Csak természetes, egészséges táplálék</p>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">🤖</div>
                    <h3 class="benefit-title">Automatikus Heti Szállítás</h3>
                    <p class="benefit-description">Soha ne felejts el rendelni - minden vasárnap automatikusan!</p>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">🏆</div>
                    <h3 class="benefit-title">15 Év Tapasztalat</h3>
                    <p class="benefit-description">Szakértő csapat segít</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Bestselling Products -->
    <section class="bestselling" id="products">
        <div class="container">
            <h2 class="section-title">Legnépszerűbb Termékek</h2>
            
            <div class="category-filter">
                <div class="filter-buttons">
                    <button class="filter-btn active" onclick="filterProducts('all')">Összes</button>
                    <button class="filter-btn" onclick="filterProducts('rovarok')">Rovarok</button>
                    <button class="filter-btn" onclick="filterProducts('hullok')">Hüllők</button>
                    <button class="filter-btn" onclick="filterProducts('kellekek')">Kellékek</button>
                </div>
            </div>
            
            <div class="products-grid">
                <div class="product-card" data-category="rovarok">
                    <div class="product-image">
                        <img src="pic8.webp" alt="Csokicsótány" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Csokicsótány (Adult)</h3>
                        <div class="product-rating">★★★★★ (47 értékelés)</div>
                        <p class="product-description">Friss, egészséges csokicsótány adult hüllőknek. 60-80 db/adag.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Frissen fotózva - pontosan ezt a minőséget kapod!</p>
                        <div class="product-price">1.200 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="rovarok">
                    <div class="product-badge badge-popular">🔥 LEGNÉPSZERŰBB</div>
                    <div class="product-image">
                        <img src="pic9.webp" alt="Tücsök" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Tücsök (Légméret)</h3>
                        <div class="product-rating">★★★★★ (33 értékelés)</div>
                        <p class="product-description">Prémium minőségű tücsök, perfekt méretben.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Frissen fotózva - pontosan ezt a minőséget kapod!</p>
                        <div class="product-price">15.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="rovarok">
                    <div class="product-image">
                        <img src="pic10.webp" alt="Lisztkukac" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Lisztkukac (1 liter)</h3>
                        <div class="product-rating">★★★★★ (56 értékelés)</div>
                        <p class="product-description">Friss lisztkukac literenként, garantált minőség.</p>
                        <div class="product-price">4.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="hullok">
                    <div class="product-image">
                        <img src="pic11.webp" alt="Leopárdgekkó" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Leopárdgekkó</h3>
                        <div class="product-rating">★★★★★ (21 értékelés)</div>
                        <p class="product-description">Egészséges, gyönyörű leopárdgekkó állatok.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Egyénileg fotózva - pontosan ezt az állatot kapod!</p>
                        <div class="product-price">13.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="hullok">
                    <div class="product-image">
                        <img src="pic12.webp" alt="Agálma" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Agálma</h3>
                        <div class="product-rating">★★★★★ (18 értékelés)</div>
                        <p class="product-description">Egészséges agálma hüllők specialista kezelésben.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Egyénileg fotózva - pontosan ezt az állatot kapod!</p>
                        <div class="product-price">15.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="hullok">
                    <div class="product-badge badge-new">✨ ÚJ ÉRKEZÉS</div>
                    <div class="product-image">
                        <img src="pic13.webp" alt="Sisakos kaméleon" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Sisakos Kaméleon</h3>
                        <div class="product-rating">★★★★★ (12 értékelés)</div>
                        <p class="product-description">Sisakos kaméleon, gondosan kezelt állatok.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Egyénileg fotózva - pontosan ezt az állatot kapod!</p>
                        <div class="product-price">10.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="kellekek">
                    <div class="product-image">
                        <img src="pic14.webp" alt="Kókuszrost" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Kókuszrost Alom</h3>
                        <div class="product-rating">★★★★★ (42 értékelés)</div>
                        <p class="product-description">Természetes kókuszrost alom terráriumokhoz.</p>
                        <div class="product-price">600 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="kellekek">
                    <div class="product-image">
                        <img src="pic15.webp" alt="Lignocel" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Lignocel (120l)</h3>
                        <div class="product-rating">★★★★★ (28 értékelés)</div>
                        <p class="product-description">Prémium lignocel alom 120 literes kiszerelésben.</p>
                        <div class="product-price">12.000 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="rovarok">
                    <div class="product-image">
                        <img src="pic16.webp" alt="Viaszmoly" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Viaszmoly</h3>
                        <div class="product-rating">★★★★★ (36 értékelés)</div>
                        <p class="product-description">Friss viaszmoly lárvák prémium minőségben.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Frissen fotózva - pontosan ezt a minőséget kapod!</p>
                        <div class="product-price">50 Ft/db</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="rovarok">
                    <div class="product-image">
                        <img src="pic20.webp" alt="Gyászlárvák" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Gyászlárvák (1 liter)</h3>
                        <div class="product-rating">★★★★★ (29 értékelés)</div>
                        <p class="product-description">Friss gyászlárvák, garantált minőségben.</p>
                        <p style="font-size: 12px; color: #e67e22; font-weight: bold; margin: 5px 0;">📸 Frissen fotózva - pontosan ezt a minőséget kapod!</p>
                        <div class="product-price">4.500 Ft</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
                
                <div class="product-card" data-category="kellekek">
                    <div class="product-image">
                        <img src="pic21.webp" alt="Fagyasztott egér" style="width:100%; height:100%; object-fit:cover;">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">Fagyasztott Egér (7-13g)</h3>
                        <div class="product-rating">★★★★★ (52 értékelés)</div>
                        <p class="product-description">Fagyasztott egér 7-13g méretben, prémium minőség.</p>
                        <div class="product-price">140 Ft/db</div>
                        <button class="add-to-cart">Kosárba rakás</button>
                        <p class="friction-reducer">✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Comparison Table -->
    <section class="comparison">
        <div class="container">
            <h2 class="section-title">Miért Válassz Minket?</h2>
            
            <div class="comparison-table">
                <table>
                    <thead>
                        <tr>
                            <th>Szempont</th>
                            <th>Hagyományos Pet Shopok</th>
                            <th>Bug Palace</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Szállítási költségek</td>
                            <td><span class="comparison-icon">❌</span>2500-4000 Ft minden rendelésnél</td>
                            <td><span class="comparison-icon">✅</span>Ingyenes heti szállítás</td>
                        </tr>
                        <tr>
                            <td>Állatok minősége</td>
                            <td><span class="comparison-icon">❌</span>Kiszámíthatatlan, gyakran haldokló</td>
                            <td><span class="comparison-icon">✅</span>Garantáltan élő érkezés</td>
                        </tr>
                        <tr>
                            <td>Szakértelem</td>
                            <td><span class="comparison-icon">❌</span>Általános eladók, rossz tanácsok</td>
                            <td><span class="comparison-icon">✅</span>15 év hüllőspecialista tapasztalat</td>
                        </tr>
                        <tr>
                            <td>Készletgazdálkodás</td>
                            <td><span class="comparison-icon">❌</span>Gyakran nincs készleten</td>
                            <td><span class="comparison-icon">✅</span>99% készletgarancia</td>
                        </tr>
                        <tr>
                            <td>Nyitvatartás/elérhetőség</td>
                            <td><span class="comparison-icon">❌</span>Korlátozott, hétvégén zárva</td>
                            <td><span class="comparison-icon">✅</span>24/7 online rendelés</td>
                        </tr>
                        <tr>
                            <td>Havi szállítási költség</td>
                            <td><span class="comparison-icon">❌</span>10.000-16.000 Ft</td>
                            <td><span class="comparison-icon">✅</span>0 Ft előfizetéssel</td>
                        </tr>
                        <tr>
                            <td>Fotók minősége</td>
                            <td><span class="comparison-icon">❌</span>Stock fotók, nem tudod mit kapsz</td>
                            <td><span class="comparison-icon">✅</span>Egyénileg fotózott állatok</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section style="background: #f8f9fa; padding: 80px 0;">
        <div class="container">
            <h2 class="section-title">Gyakori Kérdések</h2>
            
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Mennyit spórolok a heti előfizetéssel? 
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;"><strong>Hatalmas megtakarítás!</strong> Míg máshol hetente 2000 Ft szállítási díjat fizetsz, nálunk az előfizetéssel 0 Ft. <strong>8 hét alatt 16.000 Ft, egy év alatt 104.000 Ft megtakarítás!</strong> Ez több mint 2 havi táplálékra elég pénz.</p>
                    </div>
                </div>

                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Mi az a 8 hetes elkötelezettség?
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;">A heti előfizetéshez minimum 8 hét szükséges. <strong>Ez garantálja hogy 8 hétig biztos lesz friss táplálék</strong> a hüllődnek. 8 hét után bármikor leállíthatod vagy módosíthatod. Ezalatt <strong>16.000 Ft szállítási költséget spórolsz meg!</strong></p>
                    </div>
                </div>

                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Mi van, ha meghal az állat szállítás közben? 
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;">100%-os élő érkezési garanciánk van! Ha bármilyen állat nem élve érkezik meg, azonnal pótoljuk ingyen, vagy visszatérítjük a teljes vételárat. Vasárnapi szállításainkkal minimalizáljuk ezt a kockázatot - <strong>99% élő érkezési arány!</strong></p>
                    </div>
                </div>

                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Hogyan működik az automatikus szállítás?
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;"><strong>Egyszerűbb nem is lehetne!</strong> Beállítod mit szeretnél hetente, és mi automatikusan szállítjuk minden vasárnap. <strong>Soha nem kell emlékezned a rendelésre, soha nem fogynak el a termékek.</strong> Bármikor módosíthatod mit kérsz.</p>
                    </div>
                </div>

                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Hogyan működik a skip funkció? 
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;"><strong>2 alkalommal skippelhetsz a 8 hetes program alatt!</strong> Ha útban vagy, vagy éppen nincs szükség táplálékra, egyszerűen jelezd hétfő-szerda között és kihagyjuk azt a heti szállítást. <strong>Vasárnap van a szállítás, ezért szerda a deadline.</strong> A skip ingyenes és nem számít bele a 8 hétbe!</p>
                    </div>
                </div>

                <div class="faq-item" style="background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1);">
                    <div class="faq-question" style="padding: 20px; cursor: pointer; background: #27ae60; color: white; font-weight: bold;" onclick="toggleFAQ(this)">
                        Mi van ha megszakítom az előfizetést? 
                        <span style="float: right;">+</span>
                    </div>
                    <div class="faq-answer" style="padding: 0 20px; max-height: 0; overflow: hidden; transition: all 0.3s ease;">
                        <p style="padding: 20px 0;">Az előfizetést a 8 hetes minimum időszak után bármikor megszakíthatod. <strong>FONTOS:</strong> Ha az előfizetést a 8 hét előtt szakítod meg, az addig élvezett ingyenes szállításokat utólag felszámoljuk (2.000 Ft/alkalom). Ez biztosítja a rendszer fenntarthatóságát és a többi előfizető számára az ingyenes szállítást.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section" id="cta">
        <div class="container">
            <h2 class="cta-title">"Hüllőtartó Túlélési Kézikönyv" - INGYENES Letöltés</h2>
            <p class="cta-description">
                Minden amit tudnod kell: vészelyzetek kezelése, helyes táplálás, költséghatékony megoldások, profi tippek. 15 év gyakorlat 1 PDF-ben. Add meg az email címed és máris tiéd!
            </p>
            
            <form class="cta-form" onsubmit="downloadGuide(event)">
                <input type="email" class="email-input" placeholder="Add meg az email címed..." required>
                <button type="submit" class="email-submit">LETÖLTÖM INGYEN</button>
            </form>
            <p style="font-size: 12px; color: #27ae60; text-align: center; margin: 15px 0 0 0;">
                ✅ 100% Ingyenes • Nincs spam • Azonnal letölthető
            </p>
        </div>
    </section>

    <!-- Final Closer Section -->
    <section class="final-closer">
        <div class="closer-background"></div>
        <div class="closer-content">
            <h2 class="closer-title">Egészséges Hüllők Érdemelnek Friss Táplálékot - Kezdd El Ma!</h2>
            <p class="closer-description">
                Csatlakozz a 3000+ elégedett hüllőtartóhoz akik már spórolnak időt, pénzt és idegeket. Heti automatikus szállítás, mindig friss termékek, szakértői támogatás.
            </p>
            <a href="#products" class="closer-cta">VÁLASZD A TERMÉKEKET</a>
            <p style="font-size: 12px; color: #27ae60; margin: 0;">
                ✅ Ingyenes szállítás • 30 napos visszaküldés • Pénz vissza garancia
            </p>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Bug Palace</h3>
                    <p>Magyarország vezető hüllő és terráriumspecialistája. 15 év tapasztalat, 3000+ elégedett vásárló.</p>
                </div>
                
                <div class="footer-section">
                    <h3>Gyors linkek</h3>
                    <ul>
                        <li><a href="#home">Főoldal</a></li>
                        <li><a href="#products">Termékek</a></li>
                        <li><a href="#about">Rólunk</a></li>
                        <li><a href="#contact">Kapcsolat</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Vásárlói információk</h3>
                    <ul>
                        <li><a href="aszf.html">ÁSZF</a></li>
                        <li><a href="adatvedelmi-tajekoztato.html">Adatvédelmi tájékoztató</a></li>
                        <li><a href="szallitasi-informaciok.html">Szállítási információk</a></li>
                        <li><a href="visszakuldesi-feltetelek.html">Visszaküldési feltételek</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Kapcsolat</h3>
                    <ul>
                        <li>📧 info@bugpalace.hu</li>
                        <li>📞 +36 30 123 4567</li>
                        <li>📍 Budapest, Magyarország</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Bug Palace. Minden jog fenntartva.</p>
            </div>
        </div>
    </footer>

    <script>
        // Product filtering
        function filterProducts(category) {
            const products = document.querySelectorAll('.product-card');
            const buttons = document.querySelectorAll('.filter-btn');
            
            // Update active button
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            
            // Filter products
            products.forEach(product => {
                if (category === 'all' || product.dataset.category === category) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            });
        }

        // FAQ toggle functionality
        function toggleFAQ(element) {
            const answer = element.nextElementSibling;
            const icon = element.querySelector('span');
            
            if (answer.style.maxHeight === '0px' || answer.style.maxHeight === '') {
                answer.style.maxHeight = answer.scrollHeight + 'px';
                icon.textContent = '-';
            } else {
                answer.style.maxHeight = '0px';
                icon.textContent = '+';
            }
        }

        // Benefit accordion toggle
        function toggleBenefit(element) {
            const content = element.nextElementSibling;
            const icon = element.querySelector('span');
            
            // Close all other accordions
            document.querySelectorAll('.benefit-content').forEach(item => {
                if (item !== content) {
                    item.classList.remove('active');
                    item.previousElementSibling.querySelector('span').textContent = '+';
                }
            });
            
            // Toggle current accordion
            if (content.classList.contains('active')) {
                content.classList.remove('active');
                icon.textContent = '+';
            } else {
                content.classList.add('active');
                icon.textContent = '-';
            }
        }

        // Premium product purchase handler
        function handlePremiumPurchase() {
            alert('🏆 EXKLUZÍV MEGRENDELÉS!\n\nKöszönjük érdeklődését a ritka Albino Leopárdgekkó Pár iránt!\n\n✅ VIP ügyfélszolgálat felveszi Önnel a kapcsolatot 24 órán belül\n✅ Személyes konzultáció a tenyésztési lehetőségekről\n✅ Exkluzív VIP szállítás vagy személyes átadás\n\nHamarosan hírt adunk a következő lépésekről!');
        }

        // Starter package purchase handler
        function handleStarterPurchase() {
            alert('🎯 KEZDŐ CSOMAG MEGRENDELÉS!\n\nKöszönjük érdeklődését a Teljes Leopárdgekkó Kezdő Csomag iránt!\n\n✅ Minden a sikeres kezdéshez egy csomagban\n✅ 56.000 Ft megtakarítás a külön vásárláshoz képest\n✅ 3 hónapos ingyenes táplálék szállítás\n✅ 30 napos személyes támogatás\n\nHamarosan felvesszük Önnel a kapcsolatot a részletekért!');
        }

        // Hero email form submission
        function downloadHeroGuide(event) {
            event.preventDefault();
            const email = event.target.querySelector('.hero-email-input').value;
            
            if (email) {
                alert('Köszönjük! A "Hüllőtartó Túlélési Kézikönyv" hamarosan megérkezik a ' + email + ' címre!');
                event.target.querySelector('.hero-email-input').value = '';
            }
        }

        // Email form submission (CTA section)
        function downloadGuide(event) {
            event.preventDefault();
            const email = event.target.querySelector('.email-input').value;
            
            if (email) {
                alert('Köszönjük! Az útmutató hamarosan megérkezik a ' + email + ' címre!');
                event.target.querySelector('.email-input').value = '';
            }
        }

        // Simple cart functionality
        let cartCount = 0;
        const cartCountElement = document.querySelector('.cart-count');
        const addToCartButtons = document.querySelectorAll('.add-to-cart');

        addToCartButtons.forEach(button => {
            button.addEventListener('click', () => {
                cartCount++;
                cartCountElement.textContent = cartCount;
                button.textContent = 'Hozzáadva!';
                button.style.background = '#27ae60';
                
                setTimeout(() => {
                    button.textContent = 'Kosárba rakás';
                    button.style.background = '#e67e22';
                }, 1500);
            });
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('.header');
            if (window.scrollY > 100) {
                header.style.background = 'rgba(44, 62, 80, 0.95)';
            } else {
                header.style.background = 'linear-gradient(135deg, #1e3d59 0%, #2c3e50 100%)';
            }
        });
    </script>
</body>
</html>
