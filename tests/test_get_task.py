
# import pytest
# from playwright.sync_api import sync_playwright
# import os

#  # ==================================================
#     #  GET task/get-tasks-v1
#     # ==================================================

# def test_get_task():
#     with sync_playwright() as p:
#         request = p.request.new_context()

#         response = request.get(
#             "https://pmi-api-qa.irepo.in/task/get-tasks-v1",
#             headers={
#                 "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUaW1lc3RhbXAiOiIyMDI1LTEyLTE3IDE0OjM5OjU5IiwiT3JpZ2luIjoiU0YiLCJPdGhlciI6eyJTdGF0dXNQb2ludHMiOjEwMCwiU3RhdHVzTGV2ZWwiOiJUZXN0IFdpbm5lciIsIkF3YXJkUG9pbnRzIjo1NzYxOX0sIkNvbmZpZ3VyYXRpb24iOnsiSWQiOiJhN0JWZDAwMDAwMDgwY0xNQVEiLCJEVEVfSUZyYW1lVHJhZGVQcm9ncmFtX19jIjoiYTBOMjUwMDAwMDF0RGhaRUFVIiwiRFRFX0lGcmFtZVJlYXNvblR5cGVfX2MiOiJhMEZWZDAwMDAwMUo5OGZNQUMiLCJEVEVfRGVmYXVsdFJlYXNvbkRlc2NyaXB0aW9uX19jIjoiaW52aXNpYmxlIn0sIlJlbGF0ZWRBY2NvdW50cyI6W3siYXR0cmlidXRlcyI6eyJ0eXBlIjoiQWNjb3VudENvbnRhY3RSZWxhdGlvbiIsInVybCI6Ii9zZXJ2aWNlcy9kYXRhL3Y2NS4wL3NvYmplY3RzL0FjY291bnRDb250YWN0UmVsYXRpb24vMDdrVmQwMDAwMDFUeVE2SUFLIn0sIkFjY291bnRJZCI6IjAwMVZkMDAwMDA1T0V6dUlBRyIsIklkIjoiMDdrVmQwMDAwMDFUeVE2SUFLIiwiQWNjb3VudCI6eyJhdHRyaWJ1dGVzIjp7InR5cGUiOiJBY2NvdW50IiwidXJsIjoiL3NlcnZpY2VzL2RhdGEvdjY1LjAvc29iamVjdHMvQWNjb3VudC8wMDFWZDAwMDAwNU9FenVJQUcifSwiRFRFX0FjY291bnROdW1iZXJfX2MiOiJJTkRURVRyYWluaW5nX0lONiIsIkRURV9GbGV4UGFyYW1ldGVyMV9fYyI6Ik1hcmxib3JvIiwiRFRFX0ZsZXhQYXJhbWV0ZXIyX19jIjoiQUJDIiwiSWQiOiIwMDFWZDAwMDAwNU9FenVJQUcifX1dLCJzaG9wT3duZXJDb250YWN0IjpbeyJhdHRyaWJ1dGVzIjp7InR5cGUiOiJBY2NvdW50Q29udGFjdFJlbGF0aW9uIiwidXJsIjoiL3NlcnZpY2VzL2RhdGEvdjY1LjAvc29iamVjdHMvQWNjb3VudENvbnRhY3RSZWxhdGlvbi8wN2tWZDAwMDAwMVR5UTZJQUsifSwiQ29udGFjdElkIjoiMDAzVmQwMDAwMDZxWHoxSUFFIiwiQWNjb3VudElkIjoiMDAxVmQwMDAwMDVPRXp1SUFHIiwiSWQiOiIwN2tWZDAwMDAwMVR5UTZJQUsifV0sIlVzZXIiOnsiYXR0cmlidXRlcyI6eyJ0eXBlIjoiVXNlciIsInVybCI6Ii9zZXJ2aWNlcy9kYXRhL3Y2NS4wL3NvYmplY3RzL1VzZXIvMDA1VmQwMDAwMDJVbDZzSUFDIn0sIkNvbnRhY3RJZCI6IjAwM1ZkMDAwMDA2cVh6MUlBRSIsIkVtYWlsIjoiZHRlLnJldGFpbGVyLjYuc28uaW5AeW9wbWFpbC5jb20iLCJGaXJzdE5hbWUiOiJEVEUgUmV0YWlsZXIgU2l4IiwiSWQiOiIwMDVWZDAwMDAwMlVsNnNJQUMiLCJMYW5ndWFnZUxvY2FsZUtleSI6ImhpIiwiTGFzdE5hbWUiOiJTTyBPTSIsIlByb2ZpbGVJZCI6IjAwZTU4MDAwMDAwejVTcEFBSSIsIkNvbnRhY3QiOnsiYXR0cmlidXRlcyI6eyJ0eXBlIjoiQ29udGFjdCIsInVybCI6Ii9zZXJ2aWNlcy9kYXRhL3Y2NS4wL3NvYmplY3RzL0NvbnRhY3QvMDAzVmQwMDAwMDZxWHoxSUFFIn0sIkFjY291bnRJZCI6IjAwMVZkMDAwMDA1T0V6dUlBRyIsIkRURV9Db250YWN0X0lkX19jIjoiSU4tRFRFVHJhaW5pbmdfU09fNiIsIkRURV9IYXNNb3RpdmF0aW9uUHJvZ3JhbV9fYyI6ZmFsc2UsIk1vYmlsZVBob25lIjoiKzkxOTczOTczMDU3NCIsIlBob25lIjoiKzkxOTczOTczMDU3NCIsIkRURV9TdGF0dXNQb2ludHNfX2MiOjEwMCwiRFRFX1JvbGVfX2MiOiJTaG9wIE93bmVyIiwiSWQiOiIwMDNWZDAwMDAwNnFYejFJQUUiLCJBY2NvdW50Ijp7ImF0dHJpYnV0ZXMiOnsidHlwZSI6IkFjY291bnQiLCJ1cmwiOiIvc2VydmljZXMvZGF0YS92NjUuMC9zb2JqZWN0cy9BY2NvdW50LzAwMVZkMDAwMDA1T0V6dUlBRyJ9LCJCaWxsaW5nQWRkcmVzcyI6eyJjaXR5IjoiTXVtYmFpIiwiY291bnRyeSI6IkluZGlhIiwiY291bnRyeUNvZGUiOiJJTiIsImdlb2NvZGVBY2N1cmFjeSI6bnVsbCwibGF0aXR1ZGUiOm51bGwsImxvbmdpdHVkZSI6bnVsbCwicG9zdGFsQ29kZSI6bnVsbCwic3RhdGUiOm51bGwsInN0YXRlQ29kZSI6bnVsbCwic3RyZWV0IjoiTG9uZyBTdCJ9LCJEVEVfQWNjb3VudF9JZF9fYyI6IklOLURURVRyYWluaW5nX0lONiIsIkRURV9BY2NvdW50TnVtYmVyX19jIjoiSU5EVEVUcmFpbmluZ19JTjYiLCJEVEVfQXNzaWduZWRUZXJyaXRvcmllc19fYyI6IkRURV9JTiwiLCJOYW1lIjoiRFRFIFNob3AgNiBJbmRpYSBUcmFpbmluZyIsIkRURV9GbGV4UGFyYW1ldGVyMV9fYyI6Ik1hcmxib3JvIiwiRFRFX0ZsZXhQYXJhbWV0ZXIyX19jIjoiQUJDIiwiSWQiOiIwMDFWZDAwMDAwNU9FenVJQUcifX0sIlByb2ZpbGUiOnsiYXR0cmlidXRlcyI6eyJ0eXBlIjoiUHJvZmlsZSIsInVybCI6Ii9zZXJ2aWNlcy9kYXRhL3Y2NS4wL3NvYmplY3RzL1Byb2ZpbGUvMDBlNTgwMDAwMDB6NVNwQUFJIn0sIk5hbWUiOiJTaG9wIE93bmVyIDEiLCJJZCI6IjAwZTU4MDAwMDAwejVTcEFBSSJ9fSwiaWF0IjoxNzY1OTYyNjAxfQ.hrJnXosZo5HUCIa-oPLBBccobmwEp1BAScFiHn-AnI4"
#             }
#         )

#         status = response.status
#         print("Status:", status)
#         print("Body:", response.text())

#         # Handle different status codes
#         if status == 200:
#             # Success: validate JSON and count
#             data = response.json()
#             completed_count = data["data"]["completed_tasks"]["count"]
#             assert completed_count == 6, f"Expected count 6 but got {completed_count}"

#         elif status == 400:
#             # Bad Request: validation error from server
#             json_data = response.json()
#             error_message = json_data.get("message", "No message")
#             pytest.fail(f"400 Bad Request: {error_message}")

#         elif status == 500:
#             # Internal Server Error
#             pytest.fail("500 Internal Server Error returned from API")

#         else:
#             # Other unexpected codes
#             pytest.fail(f"Unexpected status code received: {status}")

#         request.dispose()



#     # ==================================================
#     # POST /webhook/monthly-task-packcount
#     # ==================================================
# def test_api_post_monthly_task(playwright):

#     request = playwright.request.new_context(
#         extra_http_headers={
#             "Accept": "application/json"
#         }
#     )


#     data = {
#         "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJtb2Jpa2FzYUBwbWkuY29tIiwiaWF0IjoxNzI5Njc1NDM5fQ.ButFNYmtq41H8rfBRZkC0lpyiuaRC21ogvl05hG-fVY",
#         "published_id": 19475,
#         "packcount": 50
#     }

#     response = request.post(
#         "https://pmi-api-qa.irepo.in/webhook/monthly-task-packcount",
#         data=data
#     )

#     status = response.status
#     print("Status:", status)
#     print("Body:", response.text())

#     unified = {
#         "success": True,
#         "http_status": status,
#         "message": "",
#         "raw_response": {}
#     }

#     try:
#         json_data = response.json()
#         unified["raw_response"] = json_data
#     except:
#         json_data = {}
#         unified["raw_response"] = {}

#     if status == 200:
#         unified["message"] = "Success: Monthly packcount submitted."
#     elif status == 400:
#         unified["message"] = "Bad Request: Invalid packcount data."
#     elif status == 401:
#         unified["message"] = "Unauthorized: Invalid or expired token."
#     elif status == 500:
#         unified["message"] = "Server Error."
#     else:
#         unified["message"] = f"Unexpected status: {status}"

#     print("Unified Output:", unified)



#     # ==================================================
#     # POST webhook/monthly-task   Invalid published_id: 51783'
#     # # ==================================================
#     data = {
#         "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJtb2Jpa2FzYUBwbWkuY29tIiwiaWF0IjoxNzI5Njc1NDM5fQ.ButFNYmtq41H8rfBRZkC0lpyiuaRC21ogvl05hG-fVY",
#         "published_id": 51783,    
#         "task_id": 631,
#         "batch_id": 15,
#         "scan_data": [
#             {"variant_name": "MARLBORO FINE TOUCH", "pack_size": 10},
#             {"variant_name": "MARLBORO FINE TOUCH", "pack_size": 10}
#         ]
#     }

#     response = request.post(
#         "https://pmi-api-qa.irepo.in/webhook/monthly-task",
#         data=data
#     )

#     status = response.status
#     print("Status:", status)
#     print("Body:", response.text())

#     unified = {
#         "success": True,
#         "http_status": status,
#         "message": "",
#         "raw_response": {}
#     }

#     try:
#         json_data = response.json()
#         unified["raw_response"] = json_data
#     except:
#         json_data = {}
#         unified["raw_response"] = {}

#     if status == 200:
#         unified["message"] = "Success: Monthly scan data submitted."
#     elif status == 400:
#         unified["message"] = "Bad Request: Invalid scan data."
#     elif status == 401:
#         unified["message"] = "Unauthorized: Invalid or expired token."
#     elif status == 500:
#         unified["message"] = "Server Error."
#     else:
#         unified["message"] = f"Unexpected status: {status}"

#     print("Unified Output:", unified)


#    # ==================================================
#     #    FETCH API task/fetch-tasks?account_id=003Vd000006qXz3IAE
#    #   ==================================================

# # def test_api_fetch_tasks(playwright):

# #     # NO TOKEN NEEDED
# #     request = playwright.request.new_context(
# #         extra_http_headers={
# #             "Accept": "application/json"
# #         }
# #     )
# #     response = request.get(
# #         "https://pmi-api-qa.irepo.in/task/fetch-tasks?account_id=003Vd000006qXz3IAE"
# #     )

# #     status = response.status
# #     print("Status:", status)
# #     print("Status Text:", response.status_text)
# #     print("Headers:", response.headers)
# #     print("Body:", response.text())
# #     print("Test completed Successfully FETCHHHHH")

# #     unified = {
# #         "success": True,
# #         "http_status": status,
# #         "message": "",
# #         "raw_response": {}
# #     }

# #     try:
# #         json_data = response.json()
# #         unified["raw_response"] = json_data
# #     except:
# #         json_data = {}
# #         unified["raw_response"] = {}

# #     # Status-based messages
# #     if status == 200:
# #         unified["message"] = "Success: Fetch tasks data fetched."
# #     elif status == 401:
# #         unified["message"] = "Unauthorized (token missing or invalid)."
# #     elif status == 404:
# #         unified["message"] = "Not Found: Fetch tasks endpoint missing."
# #     elif status == 500:
# #         unified["message"] = "Server Error."
# #     else:
# #         unified["message"] = f"Unexpected status: {status}"

# #     print("\nUnified Output:", unified)

# #     if status == 200:

# #         # Example extraction (depends on your API response structure)
# #         try:
# #             total_tasks = len(json_data["data"]["tasks"])
# #             print("Extracted Total Tasks:", total_tasks)
# #         except:
# #             print("Unable to extract tasks list from response.")

# #         print("FETCH API validation completed successfully!")


# #  ================================================
#     #    CSV File upload API csv/import-data
#    #   ==================================================

# # import os
# # from playwright.sync_api import sync_playwright

# # def test_response(playwright):

# #     # Correct file path
# #     file_path = os.path.abspath(
# #         os.path.join(
# #             os.path.dirname(__file__),   # current folder -> tests/
# #             "..",                        # go up to main project
# #             "JsonFile",                  # folder name
# #             "monthly_list - Sheet6.csv"  # file name
# #         )
# #     )

# #     print("Path:", file_path)
# #     print("Exists:", os.path.exists(file_path))

# #     if not os.path.exists(file_path):
# #         raise FileNotFoundError("CSV file not found at: " + file_path)

# #     # Correct multipart structure
# #     multipart = {
# #         "file": {
# #             "name": "monthly_list.csv",
# #             "mimeType": "text/csv",
# #             "buffer": open(file_path, "rb").read()
# #         }
# #     }

# #     context = playwright.request.new_context()

# #     response = context.post(
# #         "https://pmi-api-qa.irepo.in/csv/import-data",
# #         multipart=multipart
# #     )

# #     print("Status:", response.status)
# #     print("Response:", response.json())
       

# # import os
# # import pytest


# # # ==================================================
# # # CSV UPLOAD TEST
# # # ==================================================
# def test_upload_csv(playwright):
#     # 📁 Api_testing folder
#     base_dir = os.path.dirname(os.path.abspath(__file__))

#     csv_path = os.path.join(base_dir, "monthly list - Sheet6.csv")

#     print(" CSV path:", csv_path)

#     if not os.path.exists(csv_path):
#         pytest.fail(f"CSV file not found at: {csv_path}")

#     #  Playwright API context (fixture works here)
#     request = playwright.request.new_context(
#         extra_http_headers={
#             "Accept": "application/json"
#         }
#     )

#     #  multipart form data
#     multipart = {
#         "file": {
#             "name": "monthly_task.csv",
#             "mimeType": "text/csv",
#             "buffer": open(csv_path, "rb")
#         }
#     }

#     response = request.post(
#         "https://pmi-api-qa.irepo.in/csv/import-data",
#         multipart=multipart
#     )

#     print("Status:", response.status)
#     print("Response:", response.text())

#     assert response.status == 200

# # import os
# # import pytest


# # def test_upload_csv(playwright):
# #     base_dir = os.path.dirname(os.path.abspath(__file__))
# #     csv_path = os.path.join(base_dir, "monthly list - Sheet6.csv")

# #     print("CSV path:", csv_path)

# #     if not os.path.exists(csv_path):
# #         pytest.fail(f"CSV file not found at: {csv_path}")

# #     # Read file as BYTES
# #     with open(csv_path, "rb") as f:
# #         file_bytes = f.read()

# #     request = playwright.request.new_context(
# #         extra_http_headers={
# #             "Accept": "application/json"
# #         }
# #     )

# #     #  multipart MUST receive bytes
# #     multipart = {
# #         "file": {
# #             "name": "monthly list - Sheet6.csv",
# #             "mimeType": "text/csv",
# #             "buffer": file_bytes
# #         }
# #     }

# #     response = request.post(
# #         "https://pmi-api-qa.irepo.in/csv/import-data",
# #         multipart=multipart
# #     )

# #     print("Status:", response.status)
# #     print("Response:", response.text())

# #     assert response.status == 200
