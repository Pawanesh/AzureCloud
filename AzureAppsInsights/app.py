# Import the `configure_azure_monitor()` function from the
# `azure.monitor.opentelemetry` package.
from azure.monitor.opentelemetry import configure_azure_monitor

# Import the tracing api from the `opentelemetry` package.
from opentelemetry import trace


import logging

logging.basicConfig(format = "%(asctime)s:%(levelname)s:%(message)s", level = logging.DEBUG)

logger = logging.getLogger(__name__)
file = logging.FileHandler("example.log")
stream = logging.StreamHandler()
logger.addHandler(file)
logger.addHandler(stream)

# Configure OpenTelemetry to use Azure Monitor with the specified connection
# string.
configure_azure_monitor(
    connection_string="InstrumentationKey=583070fb-4da9-4853-be17-7beb3055d420;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/",
)

# Get a tracer for the current module.
tracer = trace.get_tracer(__name__)

# Start a new span with the name "hello". This also sets this created span as the current span in this context. This span will be exported to Azure Monitor as part of the trace.
with tracer.start_as_current_span("hello"):
    print("Hello, World!")

# Wait for export to take place in the background.
input()