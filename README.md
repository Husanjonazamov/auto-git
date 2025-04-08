
### 4. `autogit` komandasini ishga tushurish

**`setup.py`** faylidagi `entry_points` bo'limida biz **`autogit`** deb nomlangan terminal komandasi ko'rsatilgan. Bu komanda, foydalanuvchi terminalga `autogit` deb yozganda, sizning dasturga kirishni ta'minlaydi.

```python
entry_points={
    "console_scripts": [
        "autogit = autogit:main",  # `autogit` komandasini ishga tushiradi
    ]
}
