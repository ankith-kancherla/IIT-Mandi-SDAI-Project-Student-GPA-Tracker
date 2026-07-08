import markdown2
html_content = open("presentation.md", "r").read()
html = markdown2.markdown(html_content, extras=["tables"])

full_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  body {{ font-family: 'Segoe UI', sans-serif; max-width: 800px; margin: 40px auto; padding: 0 40px; color: #1e293b; }}
  h1 {{ color: #1d4ed8; font-size: 2rem; margin-bottom: 5px; }}
  h2 {{ color: #1e40af; border-bottom: 2px solid #bfdbfe; padding-bottom: 6px; margin-top: 30px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th {{ background: #1d4ed8; color: white; padding: 10px 14px; text-align: left; }}
  td {{ padding: 9px 14px; border: 1px solid #e2e8f0; }}
  tr:nth-child(even) {{ background: #f8fafc; }}
  li {{ margin: 6px 0; }}
  strong {{ color: #1e40af; }}
  hr {{ border: none; border-top: 1px solid #e2e8f0; margin: 24px 0; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

open("presentation.html", "w").write(full_html)
print("Done! Open presentation.html in browser and print to PDF")