import psutil
import sys

def check_system_health():
    print("🔍 Scanning system vitals...\n")

    # 1. 取得 CPU 使用率 (監測 1 秒)
    cpu_usage = psutil.cpu_percent(interval=1)

    # 2. 取得記憶體使用率
    memory = psutil.virtual_memory()
    mem_usage = memory.percent

    # 3. 取得硬碟空間
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # 輸出漂亮的報告
    print(f"--- 🏥 OM1 System Health Report ---")
    print(f"🧠 CPU Load:    {cpu_usage}%")
    print(f"📝 Memory:      {mem_usage}% (Used: {memory.used // (1024*1024)}MB)")
    print(f"💾 Disk Space:  {disk_usage}%")
    print("-----------------------------------")

    # 判斷健康狀況
    if cpu_usage > 80 or mem_usage > 85:
        print("\n⚠️  WARNING: System is overloaded! Cooling required.")
        sys.exit(1) # 回傳錯誤代碼
    else:
        print("\n✅ System is running smoothly. Ready for mission.")
        sys.exit(0) # 回傳成功代碼

if __name__ == "__main__":
    check_system_health()
