# 🤖 AI Blog Generator 📝

**Powered by Google Gemini AI**

An interactive command-line blog content generator that uses Google's Gemini AI to create engaging blog paragraphs on any topic you specify.

## 📁 Project Structure

### Files in this folder:

- **`blog_generator.py`** - Main application file containing the complete blog generation system
- **`README.md`** - This documentation file
- **`.env`** - Environment variables file (to be created by user - contains API keys)

## 📦 Packages and Dependencies

This project uses the following Python packages:

### Core Dependencies:
- **`google-generativeai`** - Official Google Gemini AI SDK for Python
  - Used for: Connecting to and using Google's Gemini AI model
  - Purpose: Generates blog content based on user prompts

- **`python-dotenv`** - Environment variable management
  - Used for: Loading environment variables from `.env` file
  - Purpose: Securely managing API keys without hardcoding them

### Built-in Libraries:
- **`os`** - Operating system interface
  - Used for: Environment variable access and system commands (screen clearing)

- **`textwrap`** - Text wrapping utilities
  - Used for: Formatting generated blog content for better readability

- **`datetime`** - Date and time handling
  - Used for: Adding timestamps to generated blog posts

## 🔧 API Integration and Usage

### Google Gemini AI Integration

#### API Setup:
1. **Model Used**: `gemini-1.5-flash` - Google's latest fast and efficient language model
2. **Authentication**: Uses API key stored in environment variables
3. **Configuration**: 
   - Temperature: 0.3 (for consistent, focused content)
   - Max output tokens: 400 (approximately 100-150 words)

#### How the API is Used:

```python
# Model initialization
model = genai.GenerativeModel('gemini-1.5-flash')

# Content generation with custom parameters
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        max_output_tokens=400,
        temperature=0.3,
    )
)
```

#### API Features Utilized:
- **Content Generation**: Creates blog paragraphs based on user topics
- **Prompt Engineering**: Uses enhanced prompts for better content quality
- **Response Formatting**: Processes and formats AI responses for display

## 🚀 Features

### User Interface Features:
- **Colorful Terminal Output**: Uses ANSI color codes for enhanced visual experience
- **Interactive Menu System**: User-friendly command-line interface
- **Real-time Feedback**: Progress indicators and status messages
- **Session Tracking**: Counts generated paragraphs per session

### Content Features:
- **Topic-based Generation**: Users specify topics for blog paragraphs
- **Consistent Quality**: Optimized prompts ensure engaging, informative content
- **Proper Formatting**: Text wrapping and styling for better readability
- **Timestamping**: Each generated paragraph includes creation timestamp

## 🛠️ Setup Instructions

### 1. Install Required Packages:
```bash
pip install google-generativeai python-dotenv
```

### 2. Get Gemini API Key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the generated key

### 3. Create Environment File:
Create a `.env` file in the project directory and add:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the Application:
```bash
python blog_generator.py
```

## 💡 How It Works

1. **Initialization**: 
   - Loads environment variables from `.env` file
   - Configures Gemini AI with your API key
   - Displays welcome banner

2. **User Interaction**:
   - Presents menu options (Generate content or Quit)
   - Prompts user for blog topic
   - Validates input

3. **Content Generation**:
   - Sends enhanced prompt to Gemini AI
   - Processes AI response
   - Formats content with styling and timestamp

4. **Output Display**:
   - Shows generated content in formatted style
   - Tracks number of paragraphs generated
   - Provides session summary on exit

## 🎨 Visual Features

The application includes a rich visual experience with:
- **Color-coded Messages**: Different colors for success, error, warning, and info messages
- **Decorative Elements**: Banners, separators, and Unicode symbols
- **Text Formatting**: Proper wrapping and indentation for readability
- **Progress Indicators**: Visual feedback during content generation

## 🔒 Security Features

- **Environment Variables**: API keys stored securely in `.env` file
- **Error Handling**: Comprehensive error checking for API failures
- **Input Validation**: Ensures valid user input before processing

## 📝 Usage Examples

### Example Session:
```
What should this paragraph talk about? Artificial Intelligence in Healthcare

Generated content:
Topic: Artificial Intelligence in Healthcare
Generated at: 2025-07-06 14:30:25

  Artificial Intelligence is revolutionizing healthcare by enabling 
  more accurate diagnoses, personalized treatments, and improved 
  patient outcomes. Machine learning algorithms can analyze vast 
  amounts of medical data to identify patterns that human doctors 
  might miss...
```

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Blog Writing! 📝✨**