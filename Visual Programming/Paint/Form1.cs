using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Paint
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            canvas = new Bitmap(pic.Width, pic.Height);
            canvasGraphics = Graphics.FromImage(canvas);
            canvasGraphics.Clear(Color.White);
            pic.Image = canvas;
        }

        // Canvas and drawing objects
        Bitmap canvas;
        Graphics canvasGraphics;
        bool isDrawing = false;
        Point currentPoint, previousPoint;
        Pen drawingPen = new Pen(Color.Black, 1);
        Pen eraserPen = new Pen(Color.White, 20);
        int selectedTool;

        // Shape coordinate tracking
        int mouseX, mouseY;         // Current mouse position
        int startX, startY;         // Shape width/height (delta from origin)
        int originX, originY;       // Mouse-down origin point

        // Color picker
        ColorDialog colorDialog = new ColorDialog();
        Color selectedColor;

        private void btnRectangle_Click(object sender, EventArgs e)
        {
            selectedTool = 4;
        }

        private void btnLine_Click(object sender, EventArgs e)
        {
            selectedTool = 5;
        }

        private void pic_Paint(object sender, PaintEventArgs e)
        {
            Graphics previewGraphics = e.Graphics;

            if (isDrawing)
            {
                if (selectedTool == 3) // Ellipse preview
                {
                    previewGraphics.DrawEllipse(drawingPen, originX, originY, startX, startY);
                }

                if (selectedTool == 4) // Rectangle preview
                {
                    previewGraphics.DrawRectangle(drawingPen, originX, originY, startX, startY);
                }

                if (selectedTool == 5) // Line preview
                {
                    previewGraphics.DrawLine(drawingPen, originX, originY, mouseX, mouseY);
                }
            }
        }

        private void btnColor_Click(object sender, EventArgs e)
        {
            colorDialog.ShowDialog();
            selectedColor = colorDialog.Color;
            pictureColor.BackColor = colorDialog.Color;
            drawingPen.Color = colorDialog.Color;
        }

        private void btnEllipse_Click(object sender, EventArgs e)
        {
            selectedTool = 3;
        }

        private void pic_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;
            previousPoint = e.Location;

            originX = e.X;
            originY = e.Y;
        }

        static Point set_point(PictureBox pictureBox, Point inputPoint)
        {
            float scaleX = 1f * pictureBox.Width / pictureBox.Width;
            float scaleY = 1f * pictureBox.Height / pictureBox.Height;
            return new Point((int)(inputPoint.X * scaleX), (int)(inputPoint.Y * scaleY));
        }

        private void pic_MouseClick(object sender, MouseEventArgs e)
        {
            if (selectedTool == 7) // Fill tool
            {
                Point clickedPoint = set_point(pic, e.Location);
                Fill(canvas, clickedPoint.X, clickedPoint.Y, selectedColor);
            }
        }

        private void btnFill_Click(object sender, EventArgs e)
        {
            selectedTool = 7;
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();

            saveFileDialog.Filter = "JPEG Images (*.jpg)|*.jpg";
            saveFileDialog.Title = "Save File";

            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                Bitmap exportBitmap = canvas.Clone(
                    new Rectangle(0, 0, pic.Width, pic.Height),
                    canvas.PixelFormat
                );
                exportBitmap.Save(saveFileDialog.FileName, ImageFormat.Jpeg);
            }
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            canvasGraphics.Clear(Color.White);
            pic.Image = canvas;
            selectedTool = 0;
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();

            openFileDialog.Filter = "JPEG Images (*.jpg;*.jpeg)|*.jpg;*.jpeg";
            openFileDialog.Title = "Open Image";

            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                canvas = new Bitmap(openFileDialog.FileName);
                pic.Image = canvas;
            }
        }

        private void pic_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                if (selectedTool == 1) // Pencil
                {
                    currentPoint = e.Location;
                    canvasGraphics.DrawLine(drawingPen, currentPoint, previousPoint);
                    previousPoint = currentPoint;
                }

                if (selectedTool == 2) // Eraser
                {
                    currentPoint = e.Location;
                    canvasGraphics.DrawLine(eraserPen, currentPoint, previousPoint);
                    previousPoint = currentPoint;
                }
            }

            pic.Refresh();

            mouseX = e.X;
            mouseY = e.Y;
            startX = e.X - originX;
            startY = e.Y - originY;
        }

        private void btnPencil_Click(object sender, EventArgs e)
        {
            selectedTool = 1;
        }

        private void btnEraser_Click(object sender, EventArgs e)
        {
            selectedTool = 2;
        }

        private void pic_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;

            startX = mouseX - originX;
            startY = mouseY - originY;

            if (selectedTool == 3) // Commit ellipse to canvas
            {
                canvasGraphics.DrawEllipse(drawingPen, originX, originY, startX, startY);
            }

            if (selectedTool == 4) // Commit rectangle to canvas
            {
                canvasGraphics.DrawRectangle(drawingPen, originX, originY, startX, startY);
            }

            if (selectedTool == 5) // Commit line to canvas
            {
                canvasGraphics.DrawLine(drawingPen, originX, originY, mouseX, mouseY);
            }
        }

        private void validate(Bitmap targetBitmap, Stack<Point> pixelStack, int x, int y, Color oldColor, Color newColor)
        {
            Color pixelColor = targetBitmap.GetPixel(x, y);
            if (pixelColor == oldColor)
            {
                pixelStack.Push(new Point(x, y));
                targetBitmap.SetPixel(x, y, newColor);
            }
        }

        public void Fill(Bitmap targetBitmap, int startFillX, int startFillY, Color newColor)
        {
            Color oldColor = targetBitmap.GetPixel(startFillX, startFillY);
            Stack<Point> pixelStack = new Stack<Point>();
            pixelStack.Push(new Point(startFillX, startFillY));
            targetBitmap.SetPixel(startFillX, startFillY, newColor);

            if (oldColor == newColor) return;

            while (pixelStack.Count > 0)
            {
                Point currentPixel = pixelStack.Pop();

                if (currentPixel.X > 0 && currentPixel.Y > 0 &&
                    currentPixel.X < targetBitmap.Width - 1 &&
                    currentPixel.Y < targetBitmap.Height - 1)
                {
                    validate(targetBitmap, pixelStack, currentPixel.X - 1, currentPixel.Y, oldColor, newColor); // Left
                    validate(targetBitmap, pixelStack, currentPixel.X, currentPixel.Y - 1, oldColor, newColor); // Up
                    validate(targetBitmap, pixelStack, currentPixel.X + 1, currentPixel.Y, oldColor, newColor); // Right
                    validate(targetBitmap, pixelStack, currentPixel.X, currentPixel.Y + 1, oldColor, newColor); // Down
                }
            }

            pic.Refresh();
        }
    }
}