from pptx import Presentation


def create_presentation():
    prs = Presentation()
    # {
    #     "carousel_title": "Instagram Carousel Framework",
    #     "total_slides": 8,
    #     "slides": [
    #         {
    #             "slide_number": 1,
    #             "slide_type": "Hook",
    #             "headline": "AI is taking your job? Think again. 🤯",
    #             "body_text": "Swipe to see what *really* changed in tech."
    #         },
    #         {
    #             "slide_number": 2,
    #             "slide_type": "Second Chance Cover",
    #             "headline": "Netflix just proved it: Efficiency > Genius. 💸",
    #             "body_text": "Major tech players are ditching tools not because they're bad, but because they cost too much or move too slowly. This isn't about *if* AI is powerful—it’s about the **economic reality** of building software today."
    #         },
    #         {
    #             "slide_number": 3,
    #             "slide_type": "Correction",
    #             "headline": "Stop Reading Between the Lines! 🛑",
    #             "body_text": "AI isn't replacing developers. It’s changing what \"developer\" means. The skill shifts from **manual coding** to **strategic direction.**"
    #         },
    #         {
    #             "slide_number": 4,
    #             "slide_type": "Thesis",
    #             "headline": "The New Currency of Engineering 💰",
    #             "body_text": "Value isn't in lines of code. It’s in **Engineering Hours Saved.** AI tools maximize output with minimal manual effort."
    #         },
    #         {
    #             "slide_number": 5,
    #             "slide_type": "Framework (Savable Value)",
    #             "headline": "🛠️ The AI Efficiency Audit (Save This!)",
    #             "body_text": "1. **Identify Repetition:** What do you code manually every week? 2. **Measure Time:** How many hours are spent on that task? 3. **Automate/Delegate:** Can AI handle 80% of the effort? *That's your ROI.*"
    #         },
    #         {
    #             "slide_number": 6,
    #             "slide_type": "Historical Parallel",
    #             "headline": "It’s Not New. It's Just Faster. 🕰️",
    #             "body_text": "Think frameworks replacing manual HTML/CSS. Or Python simplifying C++. Tech always reduces *manual effort*, enabling bigger leaps."
    #         },
    #         {
    #             "slide_number": 7,
    #             "slide_type": "Mindset Shift",
    #             "headline": "Your Role is Now an Architect. 🏗️",
    #             "body_text": "Don't be a coder. Be the **System Designer.** Your job: Define the problem and structure the solution. AI handles the plumbing; you design the skyscraper."
    #         },
    #         {
    #             "slide_number": 8,
    #             "slide_type": "Call-to-Action",
    #             "headline": "Don't Just Swipe. ACT. 👇",
    #             "body_text": "💾 **SAVE THIS POST:** Use the \"AI Efficiency Audit\" framework on your next project plan. 📤 **SHARE TO DM:** Send this to a skeptical manager or junior developer who needs this perspective!"
    #         }
    #     ]
    # }
    slides_data = [
        {
            "title": "Slide 1: The Hook",
            "content": "Stop designing for likes. Design for dwell time.\nThe algorithm has changed."
        },
        {
            "title": "Slide 2: Second Chance Cover",
            "content": "If they scrolled past your first slide, this is what they see next.\nMake it a standalone hook that commands attention."
        },
        {
            "title": "Slide 3: The Misinterpretation",
            "content": "Most creators think aesthetic design drives growth.\nReality: Information density and readability are the true drivers of engagement."
        },
        {
            "title": "Slide 4: The New Currency",
            "content": "Time spent reading = Platform retention.\nInstagram heavily rewards content that keeps users actively engaged on the screen."
        },
        {
            "title": "Slide 5: Savable Framework Audit",
            "content": "1. Hook: Introduce the curiosity gap.\n2. Context: Explain why this matters now.\n3. Steps: Provide actionable, concise execution points.\n4. CTA: Direct the user's next action."
        },
        {
            "title": "Slide 6: Historical Context",
            "content": "Previously, curated aesthetic grids won the algorithm.\nToday, high-density value and scannable text take priority."
        },
        {
            "title": "Slide 7: The Mindset Shift",
            "content": "Stop acting strictly as a visual designer.\nStart acting as an information architect to guide the user's attention."
        },
        {
            "title": "Slide 8: Call to Action",
            "content": "Save this framework for your next carousel build.\nDirect message this to a creator who needs to optimize their content."
        }
    ]

    for slide_data in slides_data:
        # Layout 1 is the standard "Title and Content" slide
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)

        title = slide.shapes.title
        body_shape = slide.shapes.placeholders[1]

        title.text = slide_data["title"]
        body_shape.text = slide_data["content"]

    # Save to the current directory
    file_name = "Instagram_Carousel.pptx"
    prs.save(file_name)
    print(f"Success: Presentation saved as {file_name}")


if __name__ == "__main__":
    create_presentation()