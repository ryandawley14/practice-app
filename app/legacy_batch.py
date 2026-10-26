# Nightly batch job ported from a mainframe flat-file export.
# Record layout (fixed width):
#   cols 0-9    customer id
#   cols 10-39  customer name
#   cols 40-47  order date (YYYYMMDD)
#   cols 48-57  amount in cents
#   col  58     status flag (A = active, C = cancelled)

def run_batch(infile, outfile):
    f = open(infile, "r")
    lines = f.readlines()
    f.close()
    out = open(outfile, "w")
    out.write("customer_id,name,date,amount,status\n")
    i = 0
    while i < len(lines):
        rec = lines[i]
        i = i + 1
        if len(rec) < 59:
            continue
        cid = rec[0:10].strip()
        name = rec[10:40].strip()
        d = rec[40:48]
        amt = rec[48:58].strip()
        st = rec[58:59]
        if st == "C":
            continue
        date = d[0:4] + "-" + d[4:6] + "-" + d[6:8]
        dollars = int(amt) / 100
        out.write("%s,%s,%s,%.2f,%s\n" % (cid, name, date, dollars, st))
    out.close()
