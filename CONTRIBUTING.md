# How to contribute to the Anti-Brain Rot Firewall

Thank you for wanting to help protect humanity's brains! ❤️

## How to propose new rules

1. **Fork** the repository (the “Fork” button at the top right).
2. Create a new branch: `git checkout -b add-rule-youtube-lectures`
3. Edit the `protocol-v1.3.json` or `core.py` file.
4. Example of a new rule:
   ```json
   "youtube.com/watch": {
     "condition": "duration > 40min && title contains 'lecture' or 'course'",
     "score": +2
   }
 
### Note: Version 1.3 Final is stable. New suggestions are only accepted as Issues with the "v2.0-idea" tag.".
