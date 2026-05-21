# import json
# import requests
# import subprocess
# import sys
# from datetime import datetime
#
#
# def run_tests_and_send():
#     print("🏃 Running tests...")
#     subprocess.run([sys.executable, "-m", "pytest", "--alluredir=allure-results"], )
#
#     print("📊 Generating Allure report...")
#     subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"], shell=True)
#
#     print("📈 Reading statistics...")
#     with open("./allure-report/widgets/summary.json") as f:
#         s = json.load(f)['statistic']
#
#     total = s['total']
#     passed = s['passed']
#     failed = s['failed']
#     broken = s['broken']
#     skipped = s['skipped']
#     percent = round(passed / total * 100, 2) if total else 0
#
#     # Создаем ASCII диаграмму
#     passed_pct = passed / total * 100 if total else 0
#     failed_pct = failed / total * 100 if total else 0
#     broken_pct = broken / total * 100 if total else 0
#
#     width = 20
#     passed_bar = int(passed_pct / 100 * width)
#     failed_bar = int(failed_pct / 100 * width)
#     broken_bar = int(broken_pct / 100 * width)
#
#     chart = f"""
# ✅ Passed:  {'█' * passed_bar}{'░' * (width - passed_bar)} {passed_pct:.1f}%
# ❌ Failed:  {'█' * failed_bar}{'░' * (width - failed_bar)} {failed_pct:.1f}%
# 💔 Broken:  {'█' * broken_bar}{'░' * (width - broken_bar)} {broken_pct:.1f}%
# """
#
#     msg = f"""
# 📊 **Allure Report**
# {chart}
# ⏭️ Skipped: {skipped}
# 📈 Total: {total}
# 🕐 {datetime.now().strftime('%H:%M:%S')}
# """
#
#     print("📤 Sending to Telegram...")
#     token = "8697817557:AAEhmJ-llVMCTAMReO3osDnP6Ga-ROrCiSo"
#     chat_id = "-1003944292042"
#
#     response = requests.post(
#         f"https://api.telegram.org/bot{token}/sendMessage",
#         json={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}
#     )
#
#     if response.status_code == 200:
#         print("✅ Successfully sent to Telegram!")
#     else:
#         print(f"❌ Error: {response.text}")
#
#
# if __name__ == "__main__":
#     run_tests_and_send()