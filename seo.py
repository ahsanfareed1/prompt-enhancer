from flask import Flask, request, jsonify, render_template
import openai
import re
import os

app = Flask(__name__)

# Set up OpenAI API key
API_KEY = "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"
openai.api_key = API_KEY

# Calculate SEO score
def calculate_seo_score(text, keywords):
    if not text or not keywords:
        return 0
    score = 0
    for keyword in keywords:
        if keyword.lower() in text.lower():
            score += 1
    length_score = 10 if 50 <= len(text) <= 160 else 5
    return (score * 10) + length_score

# Highlight keywords
def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = re.sub(f'(?i)({keyword})', r'<span class="highlight">\1</span>', text)
    return text

# Optimize product data
def optimize_product_data(title, description):
    prompt = f"Optimize the following product data for SEO purposes:\n\nTitle: {title}\nDescription: {description}\n\nProvide an SEO-optimized title, description, alt text for the product image, and keyword suggestions."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an SEO expert helping to optimize product data."},
                {"role": "user", "content": prompt}
            ]
        )

        output = response['choices'][0]['message']['content'].strip().splitlines()
        seo_title, seo_description, alt_text, keywords = '', '', '', []

        for line in output:
            if "Title:" in line:
                seo_title = line.split(":")[1].strip()
            elif "Description:" in line:
                seo_description = line.split(":")[1].strip()
            elif "Alt Text:" in line:
                alt_text = line.split(":")[1].strip()
            elif "Keywords:" in line:
                keywords = [kw.strip() for kw in line.split(":")[1].split(',')]

        return seo_title, seo_description, alt_text, keywords
    except Exception as e:
        return str(e), str(e), str(e), []

# Flask routes
@app.route('/')
def index():
    return render_template('seo.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    data = request.json
    title = data.get('title', '')
    description = data.get('description', '')

    if not title or not description:
        return jsonify({"error": "Title and description are required!"}), 400

    # Optimize with AI
    optimized_title, optimized_description, alt_text, keywords = optimize_product_data(title, description)

    # Calculate SEO Scores
    original_score = calculate_seo_score(title + ' ' + description, keywords)
    optimized_score = calculate_seo_score(optimized_title + ' ' + optimized_description, keywords)

    # Highlight keywords
    highlighted_title = highlight_keywords(optimized_title, keywords)
    highlighted_description = highlight_keywords(optimized_description, keywords)

    # Return results
    return jsonify({
        "optimized_title": highlighted_title,
        "optimized_description": highlighted_description,
        "alt_text": alt_text,
        "keywords": keywords,
        "original_score": original_score,
        "optimized_score": optimized_score
    })

if __name__ == '__main__':
    app.run(debug=True)