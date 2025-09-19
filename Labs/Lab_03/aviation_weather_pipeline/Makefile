.PHONY: all fetch analyze clean
all: analyze

fetch:
	@echo "Starting fetch..."
	bash ./fetch_metars.sh
	@echo "Fetch done!"

analyze: fetch
	@echo "Starting analysis..."
	bash ./analyze_data.sh
	@echo "Pipeline complete!"

clean:
	@echo "Cleaning up..."
	rm -f weather_report.csv
	rm -rf raw_metars/
	@echo "Clean done!"
