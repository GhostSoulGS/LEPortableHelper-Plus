#include <windows.h>
#include <atlbase.h>
#include <tchar.h>
#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>

using namespace std;
using namespace filesystem;

int main() {

    wstring dp0;

    wchar_t vnum[512]{}; // 設置文字緩衝
    LoadString(GetModuleHandle(NULL), 101, &vnum[0], 512); // 序列標號

    path nx1(vnum);
    path n1 = nx1.parent_path();
    path num = nx1.filename();

    if (nx1.is_relative()) {
        dp0 = wstring(current_path()) + L"\\";
    }
    else {
        dp0 = L"";
    }
    path f1(dp0 + wstring(nx1)); // v00
    wstring LEProc = dp0 + wstring(n1) + L"\\LEProc.exe"; // LEP.exe

    fstream file(f1);
    if (!file.is_open()) {
        wstring num_error = L"文件 " + wstring(num) + L" 丟失";
        wstring f1_error = L"目標路徑:  " + wstring(f1);
        MessageBox(nullptr, f1_error.c_str(), num_error.c_str(), MB_ICONERROR | MB_OK);
        return 1;
    }
    string file_guid, file_run;
    getline(file, file_guid);
    getline(file, file_run);
    CA2W guid(file_guid.c_str(), CP_UTF8);
    CA2W nx2(file_run.c_str(), CP_UTF8);
    wstring f2 = dp0 + wstring(nx2); // 執行目標
    wstring Runas = L"\"" + LEProc + L"\" -runas " + wstring(guid) + L" \"" + f2 + L"\""; // 運行代碼

    if (!exists(LEProc)) {
        wstring LEProc_error = L"當前路徑: " + wstring(LEProc);
        MessageBox(nullptr, LEProc_error.c_str(), L"丟失 LEProc.exe", MB_ICONERROR | MB_OK);
        return 1;
    }

    if (!exists(f2)) {
        wstring run_error = L"當前路徑: " + wstring(f2);
        MessageBox(nullptr, run_error.c_str(), L"丟失目標檔案", MB_ICONERROR | MB_OK);
        return 1;
    }

    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));
    CreateProcess(NULL, &Runas[0], NULL, NULL, FALSE, CREATE_NEW_CONSOLE, NULL, NULL, &si, &pi);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return 0;
}