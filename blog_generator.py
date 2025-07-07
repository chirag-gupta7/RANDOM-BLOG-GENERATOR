import google.generativeai as genai
from dotenv import load_dotenv
import os
import textwrap
from datetime import datetime

# ANSI color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    """Print a beautiful banner for the blog generator"""
    banner = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    🤖 AI Blog Generator 📝                   ║
║                   Powered by Google Gemini                   ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
    print(banner)

def print_separator():
    """Print a decorative separator"""
    print(f"{Colors.OKCYAN}{'─' * 60}{Colors.ENDC}")

def print_success(message):
    """Print success message in green"""
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")

def print_error(message):
    """Print error message in red"""
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")

def print_info(message):
    """Print info message in blue"""
    print(f"{Colors.OKBLUE}ℹ️  {message}{Colors.ENDC}")

def print_warning(message):
    """Print warning message in yellow"""
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")

def setup_gemini():
    """Configure Gemini API with proper error handling"""
    try:
        print_info("Setting up Gemini AI...")
        
        # Load environment variables from .env file
        load_dotenv()
        
        # Get API key from environment variables
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        # Configure Gemini API
        genai.configure(api_key=api_key)
        print_success("Gemini AI configured successfully!")
        return True
        
    except Exception as e:
        print_error(f"Error setting up Gemini API: {e}")
        return False

def format_blog_output(content, topic):
    """Format the blog output with beautiful styling"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Wrap text to 70 characters for better readability
    wrapped_content = textwrap.fill(content, width=70, 
                                   initial_indent="  ", 
                                   subsequent_indent="  ")
    
    output = f"""
{Colors.HEADER}{Colors.BOLD}
╭─────────────────────────────────────────────────────────────╮
│  📖 Generated Blog Paragraph                                │
╰─────────────────────────────────────────────────────────────╯
{Colors.ENDC}
{Colors.OKBLUE}{Colors.BOLD}Topic:{Colors.ENDC} {Colors.OKCYAN}{topic}{Colors.ENDC}
{Colors.OKBLUE}{Colors.BOLD}Generated at:{Colors.ENDC} {Colors.WARNING}{timestamp}{Colors.ENDC}

{Colors.OKGREEN}{wrapped_content}{Colors.ENDC}

{Colors.OKCYAN}{'─' * 60}{Colors.ENDC}
"""
    return output

def generate_blog(paragraph_topic):
    """Generate a blog paragraph using Gemini AI"""
    try:
        print_info(f"Generating content about: '{paragraph_topic}'...")
        print(f"{Colors.WARNING}🔄 Please wait...{Colors.ENDC}")
        
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Enhanced prompt for better content
        prompt = f"""Write an engaging and informative paragraph about the following topic: {paragraph_topic}

Please make it:
- Well-structured and coherent
- Informative yet accessible
- Around 100-150 words
- Engaging for readers"""
        
        # Generate content with similar parameters to your OpenAI settings
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=400,  # Equivalent to max_tokens in OpenAI
                temperature=0.3,        # Same temperature as your OpenAI code
            )
        )
        
        content = response.text.strip()
        return format_blog_output(content, paragraph_topic)
    
    except Exception as e:
        return print_error(f"Error generating blog: {e}")

def get_user_input(prompt_text):
    """Get user input with styled prompt"""
    return input(f"{Colors.OKCYAN}{Colors.BOLD}{prompt_text}{Colors.ENDC}")

def main():
    """Main function with enhanced UI"""
    # Clear screen (works on most terminals)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_banner()
    
    # Setup Gemini API
    if not setup_gemini():
        print_error("Failed to initialize Gemini API. Please check your configuration.")
        print_info("Make sure you have:")
        print("   • Created a .env file in your project directory")
        print("   • Added your GEMINI_API_KEY to the .env file")
        print("   • Installed required packages: pip install google-generativeai python-dotenv")
        return
    
    print_separator()
    print(f"{Colors.OKGREEN}{Colors.BOLD}🎉 Ready to generate amazing blog content!{Colors.ENDC}")
    print_separator()
    
    blog_count = 0
    
    while True:
        print(f"\n{Colors.HEADER}{Colors.BOLD}Options:{Colors.ENDC}")
        print(f"  {Colors.OKGREEN}Y{Colors.ENDC} - Write a new paragraph")
        print(f"  {Colors.FAIL}Q{Colors.ENDC} - Quit the program")
        print(f"  {Colors.WARNING}Any other key{Colors.ENDC} - Exit")
        
        answer = get_user_input('\n🤔 What would you like to do? ').upper()
        
        if answer == 'Y':
            paragraph_topic = get_user_input('\n💭 What should this paragraph talk about? ')
            
            if paragraph_topic.strip():
                result = generate_blog(paragraph_topic)
                if result:
                    print(result)
                    blog_count += 1
                    print_success(f"Blog paragraph #{blog_count} generated successfully!")
            else:
                print_warning("Please enter a valid topic!")
                
        elif answer == 'Q':
            print_separator()
            print(f"{Colors.HEADER}{Colors.BOLD}👋 Thanks for using AI Blog Generator!{Colors.ENDC}")
            if blog_count > 0:
                print_success(f"You generated {blog_count} blog paragraph{'s' if blog_count != 1 else ''} today!")
            print(f"{Colors.OKCYAN}Happy writing! 📝✨{Colors.ENDC}")
            print_separator()
            break
        else:
            print_info("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()