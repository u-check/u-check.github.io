from PIL import Image, ImageDraw
import os

# Pfade
input_image = r"C:\Users\chris\Documents\VSCode\Website\img\U-Check_Logo_Klein.png"
output_dir = r"C:\Users\chris\Documents\VSCode\Website\img"

# Stelle sicher, dass das Ausgabeverzeichnis existiert
os.makedirs(output_dir, exist_ok=True)

# Lade das Original-Logo
try:
    logo = Image.open(input_image)
    print(f"Original-Logo geladen: {logo.size}")
    
    # Konvertiere zu RGBA falls nötig
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')
    
    # Favicon-Größen
    sizes = [
        (16, 16, "favicon-16x16.png"),
        (32, 32, "favicon-32x32.png"),
        (180, 180, "apple-touch-icon.png")
    ]
    
    for width, height, filename in sizes:
        # Erstelle ein weißes quadratisches Bild
        favicon = Image.new('RGBA', (width, height), (255, 255, 255, 255))
        
        # Berechne die Größe des Logos (95% der Favicon-Größe für Padding)
        logo_size = int(min(width, height) * 0.95)
        
        # Skaliere das Logo proportional
        logo_resized = logo.copy()
        logo_resized.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Berechne die Position zum Zentrieren
        paste_x = (width - logo_resized.width) // 2
        paste_y = (height - logo_resized.height) // 2
        
        # Füge das Logo in der Mitte ein
        favicon.paste(logo_resized, (paste_x, paste_y), logo_resized)
        
        # Speichere das Favicon
        output_path = os.path.join(output_dir, filename)
        favicon.save(output_path, 'PNG')
        print(f"✓ Erstellt: {filename} ({width}x{height})")
    
    print("\n✨ Alle Favicons erfolgreich erstellt!")
    print(f"\nDateien gespeichert in: {output_dir}")
    print("\nErstellt:")
    print("  - favicon-16x16.png (für Browser-Tabs)")
    print("  - favicon-32x32.png (für Lesezeichen)")
    print("  - apple-touch-icon.png (für iOS)")

except FileNotFoundError:
    print(f"❌ Fehler: Datei nicht gefunden: {input_image}")
    print("Bitte überprüfe den Pfad zur Logo-Datei.")
except Exception as e:
    print(f"❌ Fehler beim Erstellen der Favicons: {str(e)}")
    print("\nHinweis: Stelle sicher, dass Pillow installiert ist:")
    print("  pip install Pillow")
