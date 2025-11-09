import pandas as pd

data = [
    ["UI-001", "Showing incorrect Bengali dates",
     "1. Open homepage\n2. Compare the displayed bengali date to the actual date\n3. Observe header",
     "Bengali dates should match the current date",
     "Showing incorrect date",
     "High",
     "https://drive.google.com/file/d/1apdAl-o86lnSteTi6kKzlXhYBT4IfuSq/view?usp=sharing",
     "Chrome Browser"],

    ["UI-002", "Showing wrong social media icon for 'X'",
     "1. Open homepage\n2. Go to the footer\n3. Observe the 'X' social media logo",
     "Official logo of 'X' should be displayed",
     "Twitter logo is showing instead of 'X' logo",
     "Low",
     "https://drive.google.com/file/d/1Qeiau3K3JplnDmgNh-h4AQwAGujib2ri/view?usp=sharing",
     "Chrome Browser"],

    ["UI-003", "Missing 'Search' button or icon in input box",
     "1. Open homepage\n2. Go to the Search Bar and type something",
     "Search input field should contain a visible 'Search' button or magnifier icon",
     "Search icon/button is missing, making it unclear how to initiate a search",
     "Low",
     "https://drive.google.com/file/d/1NPt322yYa6KpA6c6BrZ_SAY0friGpZvc/view?usp=sharing",
     "Chrome Browser"],

    ["MobileUI_001", "Missing 'Search' feature in home page",
     "1. Open homepage\n2. Browse through the home page",
     "Search should be given in the home page",
     "No search feature in home page. User has to go to hamburger menu then search",
     "Medium",
     "https://drive.google.com/file/d/1MswL9A0JpQB6VPFNtctgYNz-9172clXt/view?usp=sharing",
     "Android (Chrome)"],

    ["UI-004", "Unreadable Font Color for Initial Articles on Homepage in Dark Mode",
     "1. Open homepage\n2. Observe featured article headline text in the first section",
     "Text must be readable with sufficient contrast",
     "Contrast of the heading text is very low with black background",
     "High",
     "https://drive.google.com/file/d/1LsHtXtC0RjFD_bxUM35xP5Skj-5dZThb/view?usp=sharing",
     "Chrome Browser (Dark Mode)"],

    ["UI-005", "Middle Article Section Misaligns After Advertisement Removal",
     "1. Open homepage and observe the first articles section\n2. Remove the advertisement box of the middle section to observe the upper alignment issue",
     "Layout spacing and alignment should remain consistent",
     "The middle article section doesn't align with the other surrounding articles",
     "Medium",
     "https://drive.google.com/file/d/1uMbfMAgYeuGiCr44kAimupqjcTuEYpR7/view?usp=sharing",
     "Chrome Browser"],

    ["UI-006", "Advertisement section fitting issues",
     "1. Open homepage\n2. Observe the advertisement box in the first article section",
     "Advertisement box and cross button should fit accurately",
     "Advertisement box is not fitting perfectly, overflowing the cross button from the box",
     "Low",
     "https://drive.google.com/file/d/1KpWG5ICjrHN0iUiIB1iZkcAjlDG0paPZ/view?usp=sharing",
     "Chrome Browser"],

    ["UI-007", "Inconsistent Black Font Color in News Articles Affecting Readability",
     "1. Open several articles\n2. Observe paragraph and heading text colors\n3. Compare readability across pages",
     "All text should maintain consistent color",
     "Some articles display lighter black/gray text, reducing clarity",
     "High",
     "https://drive.google.com/drive/folders/12bFSe7lRYLmnII0Y-QBzNFerAZiYCGYl?usp=sharing",
     "Chrome Browser (Dark Mode)"],

    ["UI-008", "Inconsistent Paragraph Alignment in Privacy Policy Page",
     "1. Open homepage and go to 'শর্তাবলি ও নীতিমালা' in the footer section\n2. Observe paragraph and heading alignments throughout the page",
     "Paragraphs and headings should maintain consistent left alignment",
     "Some paragraphs are centered or misaligned, breaking consistency",
     "Medium",
     "https://drive.google.com/file/d/1wWuC8dMD_GlkzPuk9QKHO-w-aFL4M_g6/view?usp=sharing",
     "Chrome Browser"]
]

columns = ["Bug ID", "Bug Title", "Steps to Reproduce", "Expected Result",
            "Actual Result", "Severity", "Screenshot", "Environment"]

df = pd.DataFrame(data, columns=columns)

file_name = "Bug_Report_ShahriarHossain.xlsx"
df.to_excel(file_name, index=False)

print("Bug report generated successfully!")