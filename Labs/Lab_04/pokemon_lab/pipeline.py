#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary


def run_production_pipeline():
    """Execute the full production pipeline: ETL + Reporting."""
    print("="*60, file=sys.stderr)
    print("STARTING PRODUCTION PIPELINE", file=sys.stderr)
    print("="*60, file=sys.stderr)
    
    # ETL Step
    print("\n[1/2] Running ETL: Updating Portfolio...", file=sys.stderr)
    update_portfolio.main()
    
    # Reporting Step
    print("\n[2/2] Generating Summary Report...", file=sys.stderr)
    generate_summary.main()
    
    print("\n" + "="*60, file=sys.stderr)
    print("PRODUCTION PIPELINE COMPLETE", file=sys.stderr)
    print("="*60 + "\n", file=sys.stderr)


if __name__ == "__main__":
    run_production_pipeline()
