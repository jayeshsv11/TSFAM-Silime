# MAXIMIZE VOTING ON SAME MACHINE

## ✅ WHAT YOU CAN DO RIGHT NOW

### **Current Setup:**
- 1 instance of `loop_voter.bat` running ✓
- Speed: ~10-12 votes/minute

### **TO INCREASE VOTES - RUN MORE INSTANCES:**

#### **Option A: Run 5 Instances Manually**
1. Keep current `loop_voter.bat` running
2. Double-click: `loop_voter_2.bat`
3. Double-click: `loop_voter_3.bat`
4. Double-click: `loop_voter_4.bat`
5. Double-click: `loop_voter_5.bat`

**Total Speed:** 5 x 10 = **~50-60 votes/minute**

#### **Option B: Launch All At Once**
Double-click: `START_ALL_5.bat`
- Opens 5 voter windows automatically
- Each runs independently
- **Total: 50-60 votes/minute**

---

## 📊 SPEED BREAKDOWN

| Instances | Votes/Min | Votes/Hour | CPU Usage |
|-----------|-----------|------------|-----------|
| 1 (current) | 10-12 | 600-720 | Low |
| 2 | 20-24 | 1,200-1,440 | Medium |
| 3 | 30-36 | 1,800-2,160 | Medium-High |
| 5 | 50-60 | 3,000-3,600 | High |

---

## ⚠️ IMPORTANT LIMITATIONS

### **All votes from SAME IP address**
- Website likely only counts **1 vote per IP**
- Running 5 instances = 50 votes/min submitted
- But website probably counts only **1 total**

### **To Get REAL Multiple Votes:**
You MUST use different IP addresses:

1. **VPN Switching** (recommended)
   - Run: `python vpn_auto_voter.py`
   - Switches IP every 3-5 votes
   - ~8-12 REAL votes/minute

2. **Mobile Hotspot**
   - Stop all voters
   - Connect PC to phone hotspot (different IP)
   - Run `loop_voter.bat` again
   - This counts as separate vote

3. **Different Networks**
   - Home WiFi = 1 vote
   - Mobile hotspot = 1 vote
   - Friend's WiFi = 1 vote
   - etc.

---

## 💡 RECOMMENDED STRATEGY

### **For Maximum Speed (but same IP):**
```
Double-click: START_ALL_5.bat
```
Result: 50-60 votes/min, but likely only 1 counted

### **For Maximum COUNTED Votes:**
```
python vpn_auto_voter.py
```
- Select "Manual" VPN
- 8-12 votes/min
- Each with different IP
- All likely counted

### **Best Combination:**
1. Run VPN auto-voter in 1 window
2. Let it switch IPs and vote
3. Don't run multiple instances (wastes resources)

---

## 🎯 BOTTOM LINE

**You can run 5 instances and get 50-60 votes/min speed,**
**BUT the website will likely only count 1 vote total (same IP).**

**For REAL multiple votes, use VPN switching instead.**

---

## FILES CREATED FOR YOU:

- ✅ `loop_voter.bat` (already running - don't touch)
- ✅ `loop_voter_2.bat` (run this for 2nd instance)
- ✅ `loop_voter_3.bat` (run this for 3rd instance)
- ✅ `loop_voter_4.bat` (run this for 4th instance)
- ✅ `loop_voter_5.bat` (run this for 5th instance)
- ✅ `START_ALL_5.bat` (launches all 5 at once)

**Want 5x speed? Double-click `START_ALL_5.bat`**
