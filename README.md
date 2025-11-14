# PyZoeyDB (Legacy Python 2 Project)

This is an older Python 2 project that I originally wrote to scrape product data from a wholesale fashion site and transform it into a structured JSON catalog for use in a Firebase-backed boutique application.

The code is intentionally kept in Python 2 style to reflect the period when it was written.

## How this data was used

This scraper was originally written in 2017 for an iOS app I built called
*Zoey Boutique*. The app consumed the generated JSON catalog and used it to:

- Render category landing pages with hero images for each section
- Display product grids with pricing, inventory, and favorite icons
- Drive product detail screens with size options, quantity selection, and add to cart
- Power cart and wishlist flows

The same catalog format is now reused in a Shopify development store, where I
experiment with mobile ecommerce experiences.


## What it does

PyZoeyDB:

1. Crawls category pages for womens, plus size, seasonal, accessories and other departments.
2. Extracts product links and writes them to `inventoryURLs.txt`.
3. Visits each product page and scrapes:
   - name and full name
   - price and unit price
   - fabric content
   - package and size scale
   - size ratio
   - description and additional description info
   - quantity in stock
   - primary image and alternate images
   - internal product code
   - category

4. Serializes each product into:
   - a single JSON file per product
   - a text snippet used for category aggregation

5. Builds:
   - `product_list.txt` containing all product codes
   - `categories.txt` containing discovered categories
   - per-category JSON files
   - a `category_lookup.json` mapping category names to file names
   - a final `zoey_boutique.json` master catalog that aggregates all categories.

This pipeline was used as a one-off data loader to generate an inventory JSON file for a boutique style frontend.

## Tech stack

- Python 2
- `requests` for HTTP requests
- `BeautifulSoup` for HTML parsing
- File based JSON storage and aggregation

## Layout

- `pyzoeydb/config.py`  
  Category URL definitions for all departments.

- `pyzoeydb/models.py`  
  Simple `Item` class and factory for scraped products.

- `pyzoeydb/scraper.py`  
  Functions that:
  - collect product URLs from category pages  
  - scrape product details  
  - write individual product JSON files and lists.

- `pyzoeydb/categorize.py`  
  Functions that:
  - normalize category names  
  - create per-category files  
  - build a category lookup map  
  - append products into their category JSON files.

- `pyzoeydb/build_master.py`  
  Combines all category JSON fragments into a single `zoey_boutique.json` master catalog.

## Running it

This project is kept for historical purposes and was originally run in a controlled environment.

## 📱 App Screenshots (2017)

Below are screenshots from the original Zoey Boutique iOS app, powered by this Python 2 data ingestion system.

| Categories | Product Grid |
|-----------|---------------|
| ![Categories](docs/zoey_2017_categories.PNG) | ![Product Grid](docs/zoey_2017_product_grid.PNG) |

| Add to Cart | Product Detail |
|-------------|----------------|
| ![Add to Cart](docs/zoey_2017_add_to_cart.PNG) | ![Product Detail](docs/zoey_2017_product_detail.PNG) |

Basic flow:

```bash
# 1. Generate inventory URLs for a given list (example)
python -c "from pyzoeydb.scraper import save_inventory_urls_to_file; \
           from pyzoeydb.config import womenList; \
           save_inventory_urls_to_file(womenList)"

# 2. Build per-product JSON files
python -c "from pyzoeydb.scraper import build_product_json_for_firebase; \
           build_product_json_for_firebase()"

# 3. Prepare category files
python -c "from pyzoeydb.categorize import create_subcategory_file_list, create_subcategory_files; \
           create_subcategory_file_list(); \
           create_subcategory_files()"

# 4. Build category lookup and append products into category files
python -c "from pyzoeydb.categorize import create_cat_lookup_file, append_to_category_files; \
           create_cat_lookup_file(); \
           append_to_category_files()"

# 5. Build the final master JSON catalog
python pyzoeydb/build_master.py

