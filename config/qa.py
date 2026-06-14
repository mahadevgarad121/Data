# 🔧 QA ENVIRONMENT CONFIGURATION

ENVIRONMENT = "qa"
STORAGE_ACCOUNT = "qastorageaccount"
STORAGE_DOMAIN = "dfs.core.windows.net"
BRONZE_CONTAINER = "bronze-qa"
SILVER_CONTAINER = "silver-qa"
GOLD_CONTAINER = "gold-qa"

# Azure AD Credentials (Update with your QA values)
APP_ID = "your-qa-app-id-here"
TENANT_ID = "your-qa-tenant-id-here"
# Note: Store CLIENT_SECRET in GitHub Secrets, not here!

# Database Configuration
DATABASE_NAME = "qa_adventure_works"
LOG_TABLE = "qa_logs"

# Cluster Configuration
CLUSTER_WORKERS = 3
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