# Table of contents

* [Introduction](../README.md)
* [Quickstart](quickstart/README.md)
  * [Deploy Airbyte](quickstart/deploy-airbyte.md)
  * [Add a Source](quickstart/add-a-source.md)
  * [Add a Destination](quickstart/add-a-destination.md)
  * [Set up a Connection](quickstart/set-up-a-connection.md)
* [Deploying Airbyte](deploying-airbyte/README.md)
  * [Local Deployment](deploying-airbyte/local-deployment.md)
  * [On AWS \(EC2\)](deploying-airbyte/on-aws-ec2.md)
  * [On AWS ECS \(Coming Soon\)](deploying-airbyte/on-aws-ecs.md)
  * [On Azure\(VM\)](deploying-airbyte/on-azure-vm-cloud-shell.md)
  * [On GCP \(Compute Engine\)](deploying-airbyte/on-gcp-compute-engine.md)
  * [On Kubernetes \(Beta\)](deploying-airbyte/on-kubernetes.md)
  * [On Oracle Cloud Infrastructure VM](deploying-airbyte/on-oci-vm.md)
* [Operator Guides](operator-guides/README.md)
  * [Upgrading Airbyte](operator-guides/upgrading-airbyte.md)
  * [Resetting Your Data](operator-guides/reset.md)
  * [Configuring the Airbyte Database](operator-guides/configuring-airbyte-db.md)
  * [Browsing Output Logs](operator-guides/browsing-output-logs.md)
  * [Using the Airflow Airbyte Operator](operator-guides/using-the-airflow-airbyte-operator.md)
  * [Windows - Browsing Local File Output](operator-guides/locating-files-local-destination.md)
  * [Transformations and Normalization](operator-guides/transformation-and-normalization/README.md)
    * [Transformations with SQL \(Part 1/3\)](operator-guides/transformation-and-normalization/transformations-with-sql.md)
    * [Transformations with dbt \(Part 2/3\)](operator-guides/transformation-and-normalization/transformations-with-dbt.md)
    * [Transformations with Airbyte \(Part 3/3\)](operator-guides/transformation-and-normalization/transformations-with-airbyte.md)
* [Connector Catalog](integrations/README.md)
  * [Sources](integrations/sources/README.md)
    * [Amazon Seller Partner](integrations/sources/amazon-seller-partner.md)
    * [Amplitude](integrations/sources/amplitude.md)
    * [Apify Dataset](integrations/sources/apify-dataset.md)
    * [Appstore](integrations/sources/appstore.md)
    * [Asana](integrations/sources/asana.md)
    * [AWS CloudTrail](integrations/sources/aws-cloudtrail.md)
    * [Braintree](integrations/sources/braintree.md)
    * [BigQuery](integrations/sources/bigquery.md)
    * [Cart](integrations/sources/cart.md)
    * [Chargebee](integrations/sources/chargebee.md)
    * [ClickHouse](integrations/sources/clickhouse.md)
    * [CockroachDB](integrations/sources/cockroachdb.md)
    * [Db2](integrations/sources/db2.md)
    * [Dixa](integrations/sources/dixa.md)
    * [Drift](integrations/sources/drift.md)
    * [Drupal](integrations/sources/drupal.md)
    * [Exchange Rates API](integrations/sources/exchangeratesapi.md)
    * [Facebook Marketing](integrations/sources/facebook-marketing.md)
    * [Files](integrations/sources/file.md)
    * [Freshdesk](integrations/sources/freshdesk.md)
    * [GitHub](integrations/sources/github.md)
    * [GitLab](integrations/sources/gitlab.md)
    * [Google Ads](integrations/sources/google-ads.md)
    * [Google Adwords](integrations/sources/google-adwords.md)
    * [Google Analytics](integrations/sources/googleanalytics.md)
    * [Google Directory](integrations/sources/google-directory.md)
    * [Google Search Console](integrations/sources/google-search-console.md)
    * [Google Sheets](integrations/sources/google-sheets.md)
    * [Google Workspace Admin Reports](integrations/sources/google-workspace-admin-reports.md)
    * [Greenhouse](integrations/sources/greenhouse.md)
    * [Harvest](integrations/sources/harvest.md)
    * [Hubspot](integrations/sources/hubspot.md)
    * [Instagram](integrations/sources/instagram.md)
    * [Intercom](integrations/sources/intercom.md)
    * [Iterable](integrations/sources/iterable.md)
    * [Jira](integrations/sources/jira.md)
    * [Klaviyo](integrations/sources/klaviyo.md)
    * [Kustomer](integrations/sources/kustomer.md)
    * [Looker](integrations/sources/looker.md)
    * [Magento](integrations/sources/magento.md)
    * [Mailchimp](integrations/sources/mailchimp.md)
    * [Marketo](integrations/sources/marketo.md)
    * [Microsoft Dynamics AX](integrations/sources/microsoft-dynamics-ax.md)
    * [Microsoft Dynamics Customer Engagement](integrations/sources/microsoft-dynamics-customer-engagement.md)
    * [Microsoft Dynamics GP](integrations/sources/microsoft-dynamics-gp.md)
    * [Microsoft Dynamics NAV](integrations/sources/microsoft-dynamics-nav.md)
    * [Microsoft SQL Server \(MSSQL\)](integrations/sources/mssql.md)
    * [Microsoft Teams](integrations/sources/microsoft-teams.md)
    * [Mixpanel](integrations/sources/mixpanel.md)
    * [Mongo DB](integrations/sources/mongodb.md)
    * [MySQL](integrations/sources/mysql.md)
    * [Okta](integrations/sources/okta.md)
    * [Oracle DB](integrations/sources/oracle.md)
    * [Oracle Peoplesoft](integrations/sources/oracle-peoplesoft.md)
    * [Oracle Siebel CRM](integrations/sources/oracle-siebel-crm.md)
    * [Paypal Transaction](integrations/sources/paypal-transaction.md)
    * [Plaid](integrations/sources/plaid.md)
    * [Pipedrive](integrations/sources/pipedrive.md)
    * [PokéAPI](integrations/sources/pokeapi.md)
    * [Postgres](integrations/sources/postgres.md)
    * [PostHog](integrations/sources/posthog.md)
    * [PrestaShop](integrations/sources/prestashop.md)
    * [Quickbooks](integrations/sources/quickbooks.md)
    * [Recharge](integrations/sources/recharge.md)
    * [Recurly](integrations/sources/recurly.md)
    * [Redshift](integrations/sources/redshift.md)
    * [S3](integrations/sources/s3.md)
    * [SAP Business One](integrations/sources/sap-business-one.md)
    * [Salesforce](integrations/sources/salesforce.md)
    * [Sendgrid](integrations/sources/sendgrid.md)
    * [Shopify](integrations/sources/shopify.md)
    * [Slack](integrations/sources/slack.md)
    * [Smartsheets](integrations/sources/smartsheets.md)
    * [Snapchat Marketing](integrations/sources/snapchat-marketing.md)
    * [Snowflake](integrations/sources/snowflake.md)
    * [Spree Commerce](integrations/sources/spree-commerce.md)
    * [Square](integrations/sources/square.md)
    * [Stripe](integrations/sources/stripe.md)
    * [Sugar CRM](integrations/sources/sugar-crm.md)
    * [SurveyMonkey](integrations/sources/surveymonkey.md)
    * [Tempo](integrations/sources/tempo.md)
    * [Twilio](integrations/sources/twilio.md)
    * [Typeform](integrations/sources/typeform.md)
    * [US Census API](integrations/sources/us-census.md)
    * [Woo Commerce](integrations/sources/woo-commerce.md)
    * [Wordpress](integrations/sources/wordpress.md)
    * [Zencart](integrations/sources/zencart.md)
    * [Zendesk Chat](integrations/sources/zendesk-chat.md)
    * [Zendesk Sunshine](integrations/sources/zendesk-sunshine.md)
    * [Zendesk Support](integrations/sources/zendesk-support.md)
    * [Zendesk Talk](integrations/sources/zendesk-talk.md)
    * [Zoom](integrations/sources/zoom.md)
    * [Zuora](integrations/sources/zuora.md)
  * [Destinations](integrations/destinations/README.md)
    * [BigQuery](integrations/destinations/bigquery.md)
    * [Google Cloud Storage (GCS)](integrations/destinations/gcs.md)
    * [Google PubSub](integrations/destinations/pubsub.md)
    * [Kafka](integrations/destinations/kafka.md)
    * [Local CSV](integrations/destinations/local-csv.md)
    * [Local JSON](integrations/destinations/local-json.md)
    * [MeiliSearch](integrations/destinations/meilisearch.md)
    * [MSSQL](integrations/destinations/mssql.md)
    * [MySQL](integrations/destinations/mysql.md)
    * [Oracle DB](integrations/destinations/oracle.md)
    * [Postgres](integrations/destinations/postgres.md)
    * [Redshift](integrations/destinations/redshift.md)
    * [S3](integrations/destinations/s3.md)
    * [Snowflake](integrations/destinations/snowflake.md)
  * [Custom or New Connector](integrations/custom-connectors.md)
* [Connector Development](connector-development/README.md)
  * [Connector Development Kit \(Python\)](connector-development/cdk-python/README.md)
    * [Basic Concepts](connector-development/cdk-python/basic-concepts.md)
    * [Defining Stream Schemas](connector-development/cdk-python/schemas.md)
    * [Full Refresh Streams](connector-development/cdk-python/full-refresh-stream.md)
    * [Incremental Streams](connector-development/cdk-python/incremental-stream.md)
    * [HTTP-API-based Connectors](connector-development/cdk-python/http-streams.md)
    * [Python Concepts](connector-development/cdk-python/python-concepts.md)
    * [Stream Slices](connector-development/cdk-python/stream_slices.md)
  * [Airbyte 101 for Connector Development](connector-development/airbyte101.md)
  * [Testing Connectors](connector-development/testing-connectors/README.md)
    * [Source Acceptance Tests Reference](connector-development/testing-connectors/source-acceptance-tests-reference.md)
  * [Tutorials](connector-development/tutorials/README.md)
    * [Python CDK Speedrun: Creating a Source](connector-development/tutorials/cdk-speedrun.md)
    * [Python CDK: Creating a HTTP API Source](connector-development/tutorials/cdk-tutorial-python-http/README.md)
      * [Getting Started](connector-development/tutorials/cdk-tutorial-python-http/0-getting-started.md)
      * [Step 1: Creating the Source](connector-development/tutorials/cdk-tutorial-python-http/1-creating-the-source.md)
      * [Step 2: Install Dependencies](connector-development/tutorials/cdk-tutorial-python-http/2-install-dependencies.md)
      * [Step 3: Define Inputs](connector-development/tutorials/cdk-tutorial-python-http/3-define-inputs.md)
      * [Step 4: Connection Checking](connector-development/tutorials/cdk-tutorial-python-http/4-connection-checking.md)
      * [Step 5: Declare the Schema](connector-development/tutorials/cdk-tutorial-python-http/5-declare-schema.md)
      * [Step 6: Read Data](connector-development/tutorials/cdk-tutorial-python-http/6-read-data.md)
      * [Step 7: Use the Connector in Airbyte](connector-development/tutorials/cdk-tutorial-python-http/7-use-connector-in-airbyte.md)
      * [Step 8: Test Connector](connector-development/tutorials/cdk-tutorial-python-http/8-test-your-connector.md)
    * [Building a Python Source](connector-development/tutorials/building-a-python-source.md)
    * [Building a Python Destination](connector-development/tutorials/building-a-python-destination.md)
    * [Building a Java Destination](connector-development/tutorials/building-a-java-destination.md)
  * [Connector Specification Reference](connector-development/connector-specification-reference.md)
  * [Best Practices](connector-development/best-practices.md)
* [Contributing to Airbyte](contributing-to-airbyte/README.md)
  * [Code of Conduct](contributing-to-airbyte/code-of-conduct.md)
  * [Developing Locally](contributing-to-airbyte/developing-locally.md)
  * [Developing on Kubernetes](contributing-to-airbyte/developing-on-kubernetes.md)
  * [Monorepo Python Development](contributing-to-airbyte/monorepo-python-development.md)
  * [Code Style](contributing-to-airbyte/code-style.md)
  * [Gradle Cheatsheet](contributing-to-airbyte/gradle-cheatsheet.md)
  * [Updating Documentation](contributing-to-airbyte/updating-documentation.md)
  * [Templates](contributing-to-airbyte/templates/README.md)
    * [Connector Doc Template](contributing-to-airbyte/templates/integration-documentation-template.md)
* [Understanding Airbyte](understanding-airbyte/README.md)
  * [A Beginner's Guide to the AirbyteCatalog](understanding-airbyte/beginners-guide-to-catalog.md)
  * [AirbyteCatalog Reference](understanding-airbyte/catalog.md)
  * [Airbyte Specification](understanding-airbyte/airbyte-specification.md)
  * [Basic Normalization](understanding-airbyte/basic-normalization.md)
  * [Connections](understanding-airbyte/connections/README.md)
    * [Full Refresh - Overwrite](understanding-airbyte/connections/full-refresh-overwrite.md)
    * [Full Refresh - Append](understanding-airbyte/connections/full-refresh-append.md)
    * [Incremental Sync - Append](understanding-airbyte/connections/incremental-append.md)
    * [Incremental Sync - Deduped History](understanding-airbyte/connections/incremental-deduped-history.md)
  * [Operations](understanding-airbyte/operations.md)
  * [High-level View](understanding-airbyte/high-level-view.md)
  * [Workers & Jobs](understanding-airbyte/jobs.md)
  * [Technical Stack](understanding-airbyte/tech-stack.md)
  * [Change Data Capture \(CDC\)](understanding-airbyte/cdc.md)
  * [Namespaces](understanding-airbyte/namespaces.md)
* [API documentation](api-documentation.md)
* [Project Overview](project-overview/README.md)
  * [Roadmap](project-overview/roadmap.md)
  * [Changelog](project-overview/changelog/README.md)
    * [Platform](project-overview/changelog/platform.md)
    * [Connectors](project-overview/changelog/connectors.md)
  * [Slack Code of Conduct](project-overview/slack-code-of-conduct.md)
  * [License](project-overview/license.md)
* [Troubleshooting](troubleshooting/README.md)
  * [On Deploying](troubleshooting/on-deploying.md)
  * [On Setting up a New Connection](troubleshooting/new-connection.md)
  * [On Running a Sync](troubleshooting/running-sync.md)
  * [On Upgrading](troubleshooting/on-upgrading.md)
* [FAQ](faq/README.md)
  * [Getting Started](faq/getting-started.md)
  * [Data Loading](faq/data-loading.md)
  * [Transformation and Schemas](faq/transformation-and-schemas.md)
  * [Security & Data Audits](faq/security-and-data-audits.md)
  * [Differences with](faq/differences-with/README.md)
    * [Fivetran vs Airbyte](faq/differences-with/fivetran-vs-airbyte.md)
    * [StitchData vs Airbyte](faq/differences-with/stitchdata-vs-airbyte.md)
    * [Singer vs Airbyte](faq/differences-with/singer-vs-airbyte.md)
    * [Pipelinewise vs Airbyte](faq/differences-with/pipelinewise-vs-airbyte.md)
    * [Meltano vs Airbyte](faq/differences-with/meltano-vs-airbyte.md)
  * [Using Non-Standard Operating Systems](faq/deploying-on-other-os.md)