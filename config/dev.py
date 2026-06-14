# 🔧 DEVELOPMENT ENVIRONMENT CONFIGURATION

ENVIRONMENT = "dev"
STORAGE_ACCOUNT = "devstorageaccount"
STORAGE_DOMAIN = "dfs.core.windows.net"
BRONZE_CONTAINER = "bronze-dev"
SILVER_CONTAINER = "silver-dev"
GOLD_CONTAINER = "gold-dev"

# Azure AD Credentials (Update with your Dev values)
APP_ID = "your-dev-app-id-here"
TENANT_ID = "your-dev-tenant-id-here"
# Note: Store CLIENT_SECRET in GitHub Secrets, not here!

# Database Configuration
DATABASE_NAME = "dev_adventure_works"
LOG_TABLE = "dev_logs"

# Cluster Configuration
CLUSTER_WORKERS = 2
CLUSTER_SPARK_VERSION = "11.3.x-scala2.12"
CLUSTER_NODE_TYPE = "i3.xlarge"

# Paths
BRONZE_PATH = f"abfss://{BRONZE_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
SILVER_PATH = f"abfss://{SILVER_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
GOLD_PATH = f"abfss://{GOLD_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"

# Feature Flags
DEBUG_MODE = True
LOG_LEVEL = "DEBUG"
RUN_VALIDATIONS = True