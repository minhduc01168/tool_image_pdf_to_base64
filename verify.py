import base64
import os

def test_conversion():
    # Create a dummy file
    dummy_content = b"Hello Streamlit! This is a test."
    filename = "test_file.txt"
    
    with open(filename, "wb") as f:
        f.write(dummy_content)
        
    print(f"Created {filename} with content: {dummy_content}")
    
    # Simulate App Logic
    with open(filename, "rb") as f:
        bytes_data = f.read()
        
    base64_bytes = base64.b64encode(bytes_data)
    base64_string = base64_bytes.decode('utf-8')
    
    print(f"Base64 String: {base64_string}")
    
    # Verify Decoding
    decoded_bytes = base64.b64decode(base64_string)
    
    if decoded_bytes == dummy_content:
        print("✅ SUCCESS: Decoded content matches original.")
    else:
        print("❌ FAILURE: Content mismatch.")
        
    # Clean up
    os.remove(filename)

if __name__ == "__main__":
    test_conversion()
