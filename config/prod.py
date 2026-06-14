# 🔧 PRODUCTION ENVIRONMENT CONFIGURATION

ENVIRONMENT = "prod"
STORAGE_ACCOUNT = "prodstorageaccount"
STORAGE_DOMAIN = "dfs.core.windows.net"
BRONZE_CONTAINER = "bronze-prod"
SILVER_CONTAINER = "silver-prod"
GOLD_CONTAINER = "gold-prod"

# Azure AD Credentials (Update with your Prod values)
APP_ID = "your-prod-app-id-here"
TENANT_ID = "your-prod-tenant-id-here"
# Note: Store CLIENT_SECRET in GitHub Secrets, not here!

# Database Configuration
DATABASE_NAME = "prod_adventure_works"
LOG_TABLE = "prod_logs"

# Cluster Configuration
CLUSTER_WORKERS = 8
CLUSTER_SPARK_VERSION = "11.3.x-scala2.12"
CLUSTER_NODE_TYPE = "i3.2xlarge"

# Paths
BRONZE_PATH = f"abfss://{BRONZE_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
SILVER_PATH = f"abfss://{SILVER_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
GOLD_PATH = f"abfss://{GOLD_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"

# Feature Flags
DEBUG_MODE = False
LOG_LEVEL = "WARNING"
RUN_VALIDATIONS = True