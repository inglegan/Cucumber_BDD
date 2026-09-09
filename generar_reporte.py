import os
import json
import glob
from datetime import datetime

RESULTS_DIR = os.path.join("reports", "allure-results")
OUTPUT_HTML = os.path.join("reports", "reporte.html")


def build_html_report():
    os.makedirs("reports", exist_ok=True)
    json_files = glob.glob(os.path.join(RESULTS_DIR, "*-result.json"))
    if not json_files:
        print(f"No se encontraron archivos result.json en {RESULTS_DIR}")
        return

    scenarios = []
    passed_count = 0
    failed_count = 0
    broken_count = 0

    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                status = data.get("status", "unknown").lower()
                if status == "passed":
                    passed_count += 1
                elif status == "failed":
                    failed_count += 1
                else:
                    broken_count += 1

                start = data.get("start", 0)
                stop = data.get("stop", 0)
                duration = round((stop - start) / 1000, 2) if stop and start else 0.0

                status_details = data.get("statusDetails", {})
                error_msg = status_details.get("message", "")
                error_trace = status_details.get("trace", "")

                steps = []
                for step in data.get("steps", []):
                    steps.append({
                        "name": step.get("name", ""),
                        "status": step.get("status", "unknown"),
                        "duration": round((step.get("stop", 0) - step.get("start", 0)) / 1000, 2)
                    })

                scenarios.append({
                    "name": data.get("name", "Escenario sin nombre"),
                    "status": status,
                    "duration": duration,
                    "steps": steps,
                    "error_msg": error_msg,
                    "error_trace": error_trace
                })
        except Exception as e:
            print(f"Error procesando {file_path}: {e}")

    total = len(scenarios)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Ejecución BDD</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #f4f6f8; margin: 0; padding: 24px; color: #333; }}
        .container {{ max-width: 960px; margin: 0 auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); padding: 24px; }}
        h1 {{ margin-top: 0; color: #1e293b; }}
        .cards {{ display: flex; gap: 16px; margin: 20px 0; }}
        .card {{ flex: 1; padding: 16px; border-radius: 6px; text-align: center; color: #fff; font-weight: bold; }}
        .card h2 {{ margin: 0; font-size: 28px; }}
        .card p {{ margin: 4px 0 0; font-size: 14px; text-transform: uppercase; }}
        .passed-bg {{ background-color: #10b981; }}
        .failed-bg {{ background-color: #ef4444; }}
        .broken-bg {{ background-color: #f59e0b; }}
        .total-bg {{ background-color: #3b82f6; }}

        .scenario-box {{ border: 1px solid #e2e8f0; border-radius: 6px; margin-bottom: 12px; overflow: hidden; }}
        .scenario-header {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; background: #f8fafc; font-weight: 600; cursor: pointer; }}
        .badge {{ padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold; color: #fff; text-transform: uppercase; }}
        .badge-passed {{ background-color: #10b981; }}
        .badge-failed {{ background-color: #ef4444; }}
        .badge-broken {{ background-color: #f59e0b; }}

        .steps-container {{ padding: 12px 16px; border-top: 1px solid #e2e8f0; background: #fff; }}
        .step-item {{ display: flex; justify-content: space-between; padding: 6px 0; font-size: 14px; border-bottom: 1px dashed #f1f5f9; }}
        .step-name {{ color: #475569; }}
        .step-status-passed {{ color: #10b981; font-weight: bold; }}
        .step-status-failed {{ color: #ef4444; font-weight: bold; }}
        .error-log {{ margin-top: 12px; padding: 10px; background-color: #fef2f2; border-left: 4px solid #ef4444; color: #991b1b; font-family: monospace; font-size: 12px; white-space: pre-wrap; }}
    </style>
</head>
<body>
<div class="container">
    <h1>Reporte de Ejecución Automatizada</h1>
    <p>Generado el: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

    <div class="cards">
        <div class="card total-bg"><h2>{total}</h2><p>Total</p></div>
        <div class="card passed-bg"><h2>{passed_count}</h2><p>Exitosos</p></div>
        <div class="card failed-bg"><h2>{failed_count}</h2><p>Fallidos</p></div>
        <div class="card broken-bg"><h2>{broken_count}</h2><p>Errores</p></div>
    </div>

    <h3>Detalle de Escenarios</h3>
    """

    for item in scenarios:
        status_class = f"badge-{item['status']}"
        error_html = ""
        if item["error_msg"]:
            error_html = f'<div class="error-log"><strong>Fallo:</strong>\n{item["error_msg"]}\n\n{item["error_trace"]}</div>'

        steps_html = ""
        for s in item["steps"]:
            step_color = "step-status-passed" if s["status"] == "passed" else "step-status-failed"
            steps_html += f"""
            <div class="step-item">
                <span class="step-name">{s['name']}</span>
                <span class="{step_color}">{s['status']} ({s['duration']}s)</span>
            </div>
            """

        html += f"""
        <div class="scenario-box">
            <div class="scenario-header">
                <span>{item['name']} ({item['duration']}s)</span>
                <span class="badge {status_class}">{item['status']}</span>
            </div>
            <div class="steps-container">
                {steps_html}
                {error_html}
            </div>
        </div>
        """

    html += """
</div>
</body>
</html>
    """

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Reporte HTML generado con éxito en: {OUTPUT_HTML}")


if __name__ == "__main__":
    build_html_report()