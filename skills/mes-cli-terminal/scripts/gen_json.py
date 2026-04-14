import json
import sys
import os

def generate_article_json(title, content_file, menu_id=505, dict_val="其他", tags=None, article_id=None):
    if tags is None:
        tags = ["MES", "CLI"]
    
    if not os.path.exists(content_file):
        print(f"Error: File {content_file} not found.")
        sys.exit(1)
        
    with open(content_file, 'r', encoding='utf-8') as f:
        content_md = f.read()
        
    payload = {
        "title": title,
        "contentMd": content_md,
        "menuId": int(menu_id),
        "dict": dict_val,
        "tags": tags,
        "status": 2,  # Published
        "type": 0,    # Article
        "difficultLevel": 0,
        "encryptLevel": "INTERNAL"
    }
    
    if article_id is not None:
        payload["id"] = int(article_id)
    
    output_file = "article_payload.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python gen_json.py <title> <content_file> [menu_id] [dict_val] [article_id]")
    else:
        title = sys.argv[1]
        content_file = sys.argv[2]
        menu_id = sys.argv[3] if len(sys.argv) > 3 else 505
        dict_val = sys.argv[4] if len(sys.argv) > 4 else "其他"
        article_id = sys.argv[5] if len(sys.argv) > 5 else None
        
        generate_article_json(title, content_file, menu_id, dict_val, article_id=article_id)
