# 🔧 UAT ENVIRONMENT CONFIGURATION

ENVIRONMENT = "uat"
STORAGE_ACCOUNT = "uatstorageaccount"
STORAGE_DOMAIN = "dfs.core.windows.net"
BRONZE_CONTAINER = "bronze-uat"
SILVER_CONTAINER = "silver-uat"
GOLD_CONTAINER = "gold-uat"

# Azure AD Credentials (Update with your UAT values)
APP_ID = "your-uat-app-id-here"
TENANT_ID = "your-uat-tenant-id-here"
# Note: Store CLIENT_SECRET in GitHub Secrets, not here!

# Database Configuration
DATABASE_NAME = "uat_adventure_works"
LOG_TABLE = "uat_logs"

# Cluster Configuration
CLUSTER_WORKERS = 4
CLUSTER_SPARK_VERSION = "11.3.x-scala2.12"
CLUSTER_NODE_TYPE = "i3.xlarge"

# Paths
BRONZE_PATH = f"abfss://{BRONZE_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
SILVER_PATH = f"abfss://{SILVER_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"
GOLD_PATH = f"abfss://{GOLD_CONTAINER}@{STORAGE_ACCOUNT}.{STORAGE_DOMAIN}"

# Feature Flags
DEBUG_MODE = False
LOG_LEVEL = "INFO"
RUN_VALIDATIONS = True