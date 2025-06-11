# S1N CODM Checker (cdm.py)

This Python script checks Garena accounts for validity and their linkage to Call of Duty: Mobile (CODM), retrieving various account details.

**Author:** @sinontop
**Telegram Channel:** @mksln

## How It Works (Simplified)

1.  **Input:** The script takes a list of Garena accounts (in `username:password` format) from a `.txt` file.
2.  **Configuration:** It requires a link to an external PHP API script (configured via a local `.sin_init.txt` file or by user prompt). This API is crucial for fetching detailed Garena account information.
3.  **Garena Login:** For each account, it attempts to:
    *   Handle Garena's "Datadome" anti-bot measures.
    *   Securely log in to the Garena account.
4.  **Information Retrieval:**
    *   If Garena login is successful, it uses the session to query the configured external PHP API for detailed Garena account info (like email, phone, security status, shells, country, login history).
    *   It then checks if the Garena account is linked to Call of Duty: Mobile (CODM).
5.  **CODM Details:** If a CODM link is found, it retrieves CODM player details like UID, Nickname, Level, and Region.
6.  **Output:**
    *   Results are printed to the console with color-coding.
    *   Detailed information is saved into organized text files within a timestamped output folder (e.g., `sinontop-output/yourlist_check_timestamp/`):
        *   `codm-hits.txt`: Accounts with linked CODM.
        *   `garena-hits.txt`: Valid Garena accounts (CODM not linked or check failed).
        *   `invalid.txt`: Login failures or malformed input.
        *   `duplicate.txt`: Duplicates from input.
        *   `captcha-logs.txt`: Records of CAPTCHA encounters.
        *   CODM hits are also sorted by level into sub-folders.
        *   Detailed operational logs are saved.

## Basic Usage

This script is primarily designed to be run as a module through a main interface script.

1.  **Prepare Input:** Create a `.txt` file with Garena accounts, one per line (e.g., `user1:pass1`).
2.  **Configure API Link:** Ensure the `.sin_init.txt` file (in the same directory as the script) contains the correct URL for your Garena info PHP script. If not, the script will ask for it.
3.  **Run:** Execute the main script (e.g., `python main.py`). This will typically show a menu where you can select "Start CODM Checker" and then choose your input file.

## Important Notes

*   **External API Required:** The ability to fetch *detailed* Garena account information (beyond basic login validity) depends entirely on the correctly configured external PHP API script.
*   **CAPTCHA Handling:** If Garena presents a CAPTCHA, the script will pause and prompt you to change your IP address (e.g., using a VPN or restarting your router) before retrying.
*   **Datadome:** The script attempts to manage Datadome cookies. You may be prompted to enter custom Datadome values.
*   **Dependencies:** This script uses several Python packages (like `requests`, `colorama`, `pycryptodome`, `pytz`). Ensure they are installed.
*   **Responsible Use:** This tool is intended for educational and testing purposes. Use it responsibly and respect Garena's Terms of Service.