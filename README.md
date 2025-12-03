project:
  id: "H-003"
  name: "The AI Creative Studio"
  track: "Generative AI & Marketing Tech"
  tagline: "A local-first pipeline that converts a single product image into multiple ad-ready creative variants with AI-generated captions and an export-ready ZIP bundle in under 30 seconds."

1- problem_real_world_scenario:
  context: >
    Marketing teams need to rapidly produce creative variations to test messaging,
    visuals, and formats across digital advertising channels. Producing multiple variants
    of product images and captions manually is time-consuming, repetitive, and difficult
    to scale across campaigns.

  pain_point: >
    Manual creative production limits experimentation velocity and increases operational cost.
    Teams spend hours editing images, writing copy, and preparing assets, which delays
    insights and optimization cycles.

  solution_summary: >
    The AI Creative Studio automates creative generation by transforming a single product image
    into multiple stylistic variants and generating short, performance-oriented ad captions.
    All outputs are packaged into a ZIP bundle for rapid deployment.

2- expected_end_result:
  user_flow:
    input: "A product image placed in the input directory."
    action: "Run the pipeline."
    output:
      - "6 creative image variants"
      - "6 AI-generated ad captions"
      - "ZIP bundle with all assets"

  benefits:
    - "Rapid creative iteration"
    - "Reduced manual effort"
    - "Instant deployable assets"

  example_captions:
    - "Elevate your style with every step"
    - "Comfort engineered for all-day motion"
    - "Performance and aesthetics in one silhouette"

3- technical_approach:
  goal: >
    Build a lightweight, reliable system for automated creative generation
    without dependency on external image generation APIs.

  system_architecture:
    image_processing:
      description: "Generate stylistic variants locally using deterministic transformations via Pillow."
      variants:
        - "Warm tone"
        - "Cool tone"
        - "High contrast"
        - "Posterized"
        - "Blurred background"
        - "Clean standard"
    
    ai_copywriting:
      description: "Generate short, performance-focused captions using Gemini Flash."
      constraints:
        - "Max 10 words"
        - "No bullets or numbers"
        - "One caption per line"
    
    packaging:
      description: "Bundle images and captions into a ZIP file for easy distribution and deployment."

  workflow: |
    product.jpg
        ↓
    local creative transformations
        ↓
    AI caption generation
        ↓
    asset packaging
        ↓
    deployable zip bundle

4- tech_stack:
  language: "Python 3.11"
  image_engine: "Pillow"
  ai_model: "Google Gemini Flash"
  config: "python-dotenv"
  packaging: "zipfile"
  orchestration: "Python script"

  rationale: >
    The stack is optimized for speed, reliability, resource efficiency, and local execution.

5- challenges_and_learnings:
  challenge_1:
    issue: "External AI image APIs were unreliable due to permission failures, version mismatches, and rate limits."
    solution: "Switched to deterministic offline image generation."
    outcome: "Consistent, fast, and free output."

  challenge_2:
    issue: "AI-generated captions were initially verbose and inconsistent."
    solution: "Applied strict prompt constraints and output cleanup."
    outcome: "Clear, short, and usable ad copy."

6- visual_proof:
  creative_variants:
    - "Warm tone"
    - "Cool tone"
    - "High contrast"
    - "Posterized"
    - "Blurred background"
    - "Clean standard"

  exported_assets:
    - "Creative images"
    - "Captions file"
    - "ZIP bundle"

7- how_to_run:
  clone: |
    git clone https://github.com/thought1003/groundtruth-hackathon.git
    cd groundtruth-hackathon

  install_dependencies: |
    pip install pillow google-generativeai python-dotenv

  configure_api_key: |
    echo GEMINI_API_KEY="your_key_here" > .env

  add_input_image: |
    Place a product image at:
    assets/input/product.jpg

  run_pipeline: |
    python -m src.main

8- output_structure:
  directories:
    - "assets/output/images/"
    - "assets/output/captions/captions.txt"
    - "assets/output/creatives_bundle.zip"

  description: >
    Output includes image variants, captions, and a compressed ZIP archive
    ready for distribution or campaign upload.

9- future_work:
  enhancements:
    - "Background generation"
    - "Style presets"
    - "Platform-specific formats"
    - "Brand color extraction"
    - "Bulk processing"
    - "Web interface"

10- metadata:
  author: "Aryan Singh"
  event: "GroundTruth AI Hackathon"
  timeline: "December 2025"
