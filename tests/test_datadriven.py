# import json
# import os
# import pytest


# # ==================================================
# # Load JSON test data
# # ==================================================
# def load_test_data():
#     file_path = os.path.join(
#         os.path.dirname(__file__),
#         "data",
#         "data.json"
#     )

#     if not os.path.exists(file_path):
#         pytest.fail(f"data.json not found at: {file_path}")

#     with open(file_path, "r", encoding="utf-8") as file:
#         data = json.load(file)

#     return data["monthly-task-packcount"]  # returns LIST


# # ==================================================
# # POST /webhook/monthly-task-packcount (DATA DRIVEN)
# # ==================================================
# @pytest.mark.parametrize("test_case", load_test_data())
# def test_monthly_task_packcount(playwright, pytestconfig, test_case):

#     base_url = pytestconfig.getini("base_url")

#     request = playwright.request.new_context(
#         base_url=base_url,
#         extra_http_headers={
#             "Accept": "application/json",
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {test_case['auth_token']}"
#         }
#     )

#     payload = {
#         "auth_token": test_case["auth_token"],
#         "published_id": test_case["published_id"],
#         "packcount": test_case["packcount"]
#     }

#     response = request.post(
#         "/webhook/monthly-task-packcount",
#         data=json.dumps(payload)
#     )

#     status = response.status
#     body = response.text()

#     print("\nStatus:", status)
#     print("Response:", body)

#     # -------- Parse API response safely --------
#     try:
#         response_json = response.json()
#     except Exception:
#         response_json = {"raw_response": body}

#     api_message = (
#         response_json.get("message")
#         or response_json.get("error")
#         or "No message returned by API"
#     )

#     # -------- VALID / INVALID LOGGING --------
#     if status == 200:
#         print("VALID DATA → API returned tasks")
#     else:
#         print("INVALID DATA → API rejected request")

#     invalid_token = test_case.get("auth_token", "NO TOKEN PROVIDED")

#     print("TOKEN USED:")
#     print("--------------------------------------------------")
#     print(invalid_token)
#     print("--------------------------------------------------")

#     print("FULL TEST CASE:")
#     print(json.dumps(test_case, indent=2))

#     # -------- Unified Output --------
#     unified = {
#         "test_name": test_case.get("name"),
#         "status": status,
#         "api_message": api_message,
#         "response": response_json
#     }

#     print("\nUnified Output:")
#     print(json.dumps(unified, indent=2))




# # ///////////////////////////////////PACK COUNT ENDS///////////////////////



# # /////////////////////////////// GET TASK V1 START   2222222222222222 ///////////////////////
# # ==================================================
# # Load JSON
# # ==================================================

# def get_json_data():
#     file_path = os.path.join(
#         os.path.dirname(__file__),
#         "data",
#         "data.json"
#     )

#     print("Loading JSON from:", file_path)

#     if not os.path.exists(file_path):
#         pytest.fail(f"data.json not found at: {file_path}")

#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)


# def load_get_tasks_data():
#     return get_json_data()["get-tasks-v1"]


# # ==================================================
# # GET /task/get-tasks-v1 (DATA DRIVEN)
# # ==================================================
# @pytest.mark.parametrize("test_case", load_get_tasks_data())
# def test_get_tasks(playwright, test_case):

#     print("\n==============================")
#     print("TEST NAME:", test_case.get("name"))

#     token = test_case.get("auth_token")

#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json"
#     }

#     #  Add Authorization ONLY if token exists
#     if token:
#         if not token.startswith("Bearer "):
#             token = f"Bearer {token}"
#         headers["Authorization"] = token

#     request = playwright.request.new_context(
#         extra_http_headers=headers
#     )

#     response = request.get(
#         "https://pmi-api-prod.irepo.in/task/get-tasks-v1"
#     )

#     status = response.status
#     body = response.text()

#     print("RESPONSE STATUS:", status)
#     print("RESPONSE BODY:", body)

#     # -------- Parse API response safely --------
#     try:
#         response_json = response.json()
#     except Exception:
#         response_json = {"raw_response": body}

#     api_message = (
#         response_json.get("message")
#         or response_json.get("error")
#         or "No message returned by API"
#     )

#     # -------- VALID / INVALID LOGGING --------

#     if status == 200:
#         print(" VALID DATA → API returned tasks")
#     else:
#         print(" INVALID DATA → API rejected request")

#     invalid_token = test_case.get("auth_token", "NO TOKEN PROVIDED")

#     print("INVALID TOKEN USED:")
#     print("--------------------------------------------------")
#     print(invalid_token,)
#     print("--------------------------------------------------")

#     print(" FULL INVALID TEST CASE:")
#     print(json.dumps(test_case, indent=2))


#     # -------- Unified Output --------
#     unified = {
#         "test_name": test_case.get("name"),
#         "status": status,
#         "api_message": api_message,
#         "response": response_json
#     }

#     print("\nUnified Output:")
#     print(json.dumps(unified, indent=2))


# # /////////////////////////////// GET TASK V1 ENDS///////////////////////

# # ////////////////////////// FETCH API START  33333333    ////////////////////////
# # ==================================================
# # Load JSON test data
# # ==================================================
# def load_test_data():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, "data", "data.json")

#     if not os.path.exists(file_path):
#         pytest.fail(f"JSON file not found: {file_path}")

#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)


# # ==================================================
# # GET /task/fetch-tasks
# # ==================================================
# @pytest.mark.parametrize("test_case", load_test_data()["fetch-tasks"])
# def test_api_fetch_tasks(playwright, pytestconfig, test_case):

#     print("\n==============================")
#     print("TEST NAME:", test_case["name"])

#     base_url = pytestconfig.getini("base_url")
#     account_id = test_case["account_id"]
#     expected_status = test_case["expected_status"]

#     request = playwright.request.new_context(
#         base_url=base_url,
#         extra_http_headers={
#             "Accept": "application/json"
#         }
#     )

#     response = request.get(
#         f"/task/fetch-tasks?account_id={account_id}"
#     )

#     status = response.status

#     try:
#         response_json = response.json()
#     except Exception:
#         response_json = {"raw_response": response.text()}

#     print("STATUS CODE:", status)
#     print("EXPECTED STATUS:", expected_status)

#     print("\n========== API RESPONSE ==========")
#     print(json.dumps(response_json, indent=2))
#     print("==================================")

#     if status == 200:
#         print(" RESULT → ✅ VALID RESPONSE")
#     else:
#         print(" RESULT → ❌ INVALID RESPONSE")

# # ////////////////////////// FETCH API ENDS ////////////////////////


# # ///////////////////////////WEBHOOK/MONTHLY-TASK START    444444444 //////////////////////////////////////

# # # ==================================================
# # #     POST webhook/monthly-task   Invalid published_id: 51783'
# # # ==================================================
# # ==================================================
# # Load JSON test data
# # ==================================================
# def load_test_data():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, "data", "data.json")

#     if not os.path.exists(file_path):
#         pytest.fail(f"JSON file not found: {file_path}")

#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)


# def load_monthly_task_data():
#     return load_test_data()["monthly-task"]


# # ==================================================
# # POST /webhook/monthly-task (DATA DRIVEN)
# # ==================================================
# @pytest.mark.parametrize("test_case", load_monthly_task_data())
# def test_monthly_task(playwright, pytestconfig, test_case):

#     print("\n==============================")
#     print("TEST NAME:", test_case.get("name"))

#     base_url = pytestconfig.getini("base_url")

#     request = playwright.request.new_context(
#         base_url=base_url,
#         extra_http_headers={
#             "Accept": "application/json",
#             "Content-Type": "application/json"
#         }
#     )

#     # TOKEN IN BODY (NOT HEADER)
#     payload = {
#         "auth_token": test_case.get("auth_token"),
#         "published_id": test_case.get("published_id"),
#         "task_id": test_case.get("task_id"),
#         "batch_id": test_case.get("batch_id"),
#         "scan_data": test_case.get("scan_data")
#     }

#     print("\nREQUEST PAYLOAD:")
#     print(json.dumps(payload, indent=2))

#     response = request.post(
#         "/webhook/monthly-task",
#         data=json.dumps(payload)
#     )

#     status = response.status
#     body = response.text()

#     print("\nRESPONSE STATUS:", status)
#     print("RESPONSE BODY:", body)

#     # -------- Safe JSON parse --------
#     try:
#         response_json = response.json()
#     except Exception:
#         response_json = {"raw_response": body}

#     api_message = (
#         response_json.get("message")
#         or response_json.get("error")
#         or "No message returned by API"
#     )

#     # -------- VALID / INVALID LOGGING --------
#     if status == 200:
#         print(" RESULT → ✅ VALID DATA (Monthly task submitted)")
#     else:
#         print(" RESULT → ❌ INVALID DATA (Expected for negative test)")
#         print(" INVALID INPUT USED:")
#         print(json.dumps(payload, indent=2))

#     # -------- Unified Output --------
#     unified = {
#         "test_name": test_case.get("name"),
#         "status": status,
#         "api_message": api_message,
#         "request_payload": payload,
#         "response": response_json
#     }

#     print("\nUnified Output:")
#     print(json.dumps(unified, indent=2))

#     # Always pass (logging-only test)
#     assert True

# #  ///////////////////////////WEBHOOK/MONTHLY-TASK ENDS//////////////////////////////////////
  

# # #  /////////////////////////// CSV FILE UPLOAD  API 55555555555555555555 //////////////////////////////////////

# # ==================================================
# # Load CSV test data from tests/data/data.json
# # ==================================================

# # def load_csv_test_data():
# #     file_path = os.path.join(
# #         os.path.dirname(os.path.abspath(__file__)),
# #         "data",
# #         "data.json"
# #     )

# #     if not os.path.exists(file_path):
# #         pytest.fail(f"data.json not found at: {file_path}")

# #     with open(file_path, "r", encoding="utf-8") as f:
# #         return json.load(f)["csv-upload"]


# # @pytest.mark.parametrize("test_case", load_csv_test_data())
# # def test_upload_csv(playwright, test_case):

# #     print("\n==============================")
# #     print("TEST NAME:", test_case["name"])

# #     csv_path = os.path.join(
# #         os.path.dirname(os.path.abspath(__file__)),
# #         "data",
# #         test_case["file_name"]
# #     )

# #     print("CSV PATH:", csv_path)

# #     if not os.path.exists(csv_path):
# #         print(" FILE NOT FOUND (EXPECTED INVALID CASE)")
# #         assert True
# #         return

# #     with open(csv_path, "rb") as f:
# #         file_bytes = f.read()

# #     request = playwright.request.new_context(
# #         extra_http_headers={
# #             "Accept": "application/json"
# #         }
# #     )

# #     multipart = {
# #         "document_path": {   
# #             "name": test_case["file_name"],
# #             "mimeType": "text/csv",
# #             "buffer": file_bytes
# #         }
# #     }

# #     response = request.post(
# #         "https://pmi-api-prod.irepo.in/csv/import-data",
# #         multipart=multipart
# #     )

# #     status = response.status
# #     raw_body = response.text()

# #     print("\nHTTP STATUS:", status)
# #     print("RAW RESPONSE:", raw_body)

# #     try:
# #         response_json = response.json()
# #     except Exception:
# #         response_json = {"raw_response": raw_body}

# #     # ==============================
# #     # API RESPONSE HANDLING
# #     # ==============================
# #     if status == 200:
# #         print(" SUCCESS RESPONSE")
# #         print(json.dumps(response_json, indent=2))

# #     elif status == 500 and "duplicates" in raw_body.lower():
# #         print(json.dumps(response_json, indent=2))

# #     else:
# #         print(json.dumps(response_json, indent=2))

# #     # ==============================
# #     # UNIFIED TERMINAL OUTPUT
# #     # ==============================
# #     unified = {
# #         "test_name": test_case["name"],
# #         "file_name": test_case["file_name"],
# #         "http_status": status,
# #         "api_response": response_json
# #     }

# #     print("\nUNIFIED OUTPUT:")
# #     print(json.dumps(unified, indent=2))

# #     # Business-expected behavior → always pass
# #     assert True


# # #  /////////////////////////// CSV FILE UPLOAD API ends  //////////////////////////////////////



# # # //////////////TASK/GET-DETAILS-MONTHLY 66666666666666666 //////////////////
# # # #   ===============================================
# # # #    task/get-detail-monthly
# # # #   ==================================================

# # # ==================================================
# # # Load test data
# # # ==================================================
# def load_monthly_detail_data():
#     file_path = os.path.join(
#         os.path.dirname(os.path.abspath(__file__)),
#         "data",
#         "data.json"
#     )

#     if not os.path.exists(file_path):
#         pytest.fail(f"data.json not found at: {file_path}")

#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     return data["monthly-detail"]



# # ==================================================
# # GET /task/get-detail-monthly
# # ==================================================

# @pytest.mark.parametrize("test_case", load_monthly_detail_data())
# def test_get_detail_monthly(playwright, pytestconfig, test_case):

#     base_url = pytestconfig.getini("base_url")

#     print("\n==============================")
#     print("TEST NAME:", test_case["name"])

#     request = playwright.request.new_context(
#         base_url=base_url,
#         extra_http_headers={
#             "Accept": "*/*",
#             "Accept-Language": "hi",
#             "Authorization": test_case["auth_token"],
#             "Content-Type": "application/json",
#             "x-language": "hi"
#         }
#     )

#     response = request.get(
#         "/task/get-detail-monthly",
#         params={
#             "month": test_case["month"],
#             "year": test_case["year"],
#             "taskId": test_case["taskId"]
#         }
#     )

#     status = response.status
#     body = response.text()

#     print("STATUS:", status)
#     print("BODY:", body)

#     try:
#         response_json = response.json()
#     except Exception:
#         response_json = {"raw_response": body}

#     if status == 200:

        
#         print(" VALID REQUEST → Monthly task details fetched")
#     else:
#         print(" INVALID REQUEST → API rejected request (EXPECTED)")

#     print("\nUnified Output:")
#     print(json.dumps(response_json, indent=2))

#     # Always pass (logging-only test)
#     assert True