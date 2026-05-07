import asyncio
import os
from playwright.async_api import async_playwright

async def html_to_pdf():
    async with async_playwright() as p:
        # Get absolute path to the HTML file
        current_dir = os.getcwd()
        html_path = f"file:///{os.path.join(current_dir, 'gay_types_presentation.html')}".replace('\\', '/')
        pdf_path = os.path.join(current_dir, 'gay_types_presentation.pdf')

        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Open the file
        await page.goto(html_path)
        
        # Give some time for fonts to load
        await asyncio.sleep(2)

        # PDF options: landscape, one slide per page (assuming slides are 100vh)
        # We use print_background=True to keep the neon colors
        await page.pdf(
            path=pdf_path,
            format="A4",
            landscape=True,
            print_background=True,
            display_header_footer=False,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )

        await browser.close()
        print(f"PDF generated successfully at: {pdf_path}")

if __name__ == "__main__":
    asyncio.run(html_to_pdf())
