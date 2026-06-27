namespace Paint
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.panel1 = new System.Windows.Forms.Panel();
            this.btnLine = new System.Windows.Forms.Button();
            this.btnRectangle = new System.Windows.Forms.Button();
            this.btnEllipse = new System.Windows.Forms.Button();
            this.btnEraser = new System.Windows.Forms.Button();
            this.btnPencil = new System.Windows.Forms.Button();
            this.btnFill = new System.Windows.Forms.Button();
            this.btnColor = new System.Windows.Forms.Button();
            this.pictureColor = new System.Windows.Forms.Button();
            this.pic = new System.Windows.Forms.PictureBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pic)).BeginInit();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.panel1.Controls.Add(this.btnLine);
            this.panel1.Controls.Add(this.btnRectangle);
            this.panel1.Controls.Add(this.btnEllipse);
            this.panel1.Controls.Add(this.btnEraser);
            this.panel1.Controls.Add(this.btnPencil);
            this.panel1.Controls.Add(this.btnFill);
            this.panel1.Controls.Add(this.btnColor);
            this.panel1.Controls.Add(this.pictureColor);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 24);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(87, 637);
            this.panel1.TabIndex = 1;
            // 
            // btnLine
            // 
            this.btnLine.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnLine.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnLine.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnLine.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnLine.ForeColor = System.Drawing.Color.Black;
            this.btnLine.Image = global::Paint.Properties.Resources.line;
            this.btnLine.Location = new System.Drawing.Point(12, 356);
            this.btnLine.Name = "btnLine";
            this.btnLine.Size = new System.Drawing.Size(67, 72);
            this.btnLine.TabIndex = 7;
            this.btnLine.Text = "Line";
            this.btnLine.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnLine.UseVisualStyleBackColor = true;
            this.btnLine.Click += new System.EventHandler(this.btnLine_Click);
            // 
            // btnRectangle
            // 
            this.btnRectangle.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnRectangle.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnRectangle.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnRectangle.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnRectangle.ForeColor = System.Drawing.Color.Black;
            this.btnRectangle.Image = global::Paint.Properties.Resources.rectangle;
            this.btnRectangle.Location = new System.Drawing.Point(12, 518);
            this.btnRectangle.Margin = new System.Windows.Forms.Padding(5);
            this.btnRectangle.Name = "btnRectangle";
            this.btnRectangle.Size = new System.Drawing.Size(67, 75);
            this.btnRectangle.TabIndex = 6;
            this.btnRectangle.Text = "Rectangle";
            this.btnRectangle.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnRectangle.UseVisualStyleBackColor = true;
            this.btnRectangle.Click += new System.EventHandler(this.btnRectangle_Click);
            // 
            // btnEllipse
            // 
            this.btnEllipse.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnEllipse.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnEllipse.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnEllipse.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnEllipse.ForeColor = System.Drawing.Color.Black;
            this.btnEllipse.Image = global::Paint.Properties.Resources.circle;
            this.btnEllipse.Location = new System.Drawing.Point(12, 434);
            this.btnEllipse.Name = "btnEllipse";
            this.btnEllipse.Size = new System.Drawing.Size(67, 76);
            this.btnEllipse.TabIndex = 5;
            this.btnEllipse.Text = "Ellipse";
            this.btnEllipse.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnEllipse.UseVisualStyleBackColor = true;
            this.btnEllipse.Click += new System.EventHandler(this.btnEllipse_Click);
            // 
            // btnEraser
            // 
            this.btnEraser.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnEraser.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnEraser.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnEraser.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnEraser.ForeColor = System.Drawing.Color.Black;
            this.btnEraser.Image = global::Paint.Properties.Resources.eraser;
            this.btnEraser.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnEraser.Location = new System.Drawing.Point(12, 199);
            this.btnEraser.Name = "btnEraser";
            this.btnEraser.Size = new System.Drawing.Size(67, 75);
            this.btnEraser.TabIndex = 4;
            this.btnEraser.Text = "Eraser";
            this.btnEraser.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnEraser.UseVisualStyleBackColor = true;
            this.btnEraser.Click += new System.EventHandler(this.btnEraser_Click);
            // 
            // btnPencil
            // 
            this.btnPencil.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnPencil.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnPencil.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnPencil.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnPencil.ForeColor = System.Drawing.Color.Black;
            this.btnPencil.Image = global::Paint.Properties.Resources.pencil;
            this.btnPencil.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnPencil.Location = new System.Drawing.Point(12, 280);
            this.btnPencil.Name = "btnPencil";
            this.btnPencil.Size = new System.Drawing.Size(67, 70);
            this.btnPencil.TabIndex = 3;
            this.btnPencil.Text = "Pencil";
            this.btnPencil.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnPencil.UseVisualStyleBackColor = true;
            this.btnPencil.Click += new System.EventHandler(this.btnPencil_Click);
            // 
            // btnFill
            // 
            this.btnFill.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnFill.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnFill.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnFill.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnFill.ForeColor = System.Drawing.Color.Black;
            this.btnFill.Image = global::Paint.Properties.Resources.bucket;
            this.btnFill.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnFill.Location = new System.Drawing.Point(12, 124);
            this.btnFill.Name = "btnFill";
            this.btnFill.Size = new System.Drawing.Size(67, 69);
            this.btnFill.TabIndex = 2;
            this.btnFill.Text = "Fill";
            this.btnFill.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnFill.UseVisualStyleBackColor = true;
            this.btnFill.Click += new System.EventHandler(this.btnFill_Click);
            // 
            // btnColor
            // 
            this.btnColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnColor.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Gray;
            this.btnColor.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.btnColor.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnColor.ForeColor = System.Drawing.Color.Black;
            this.btnColor.Image = global::Paint.Properties.Resources.color;
            this.btnColor.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnColor.Location = new System.Drawing.Point(12, 49);
            this.btnColor.Name = "btnColor";
            this.btnColor.Size = new System.Drawing.Size(67, 69);
            this.btnColor.TabIndex = 1;
            this.btnColor.Text = "Color";
            this.btnColor.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.btnColor.UseVisualStyleBackColor = true;
            this.btnColor.Click += new System.EventHandler(this.btnColor_Click);
            // 
            // pictureColor
            // 
            this.pictureColor.BackColor = System.Drawing.Color.White;
            this.pictureColor.Location = new System.Drawing.Point(12, 12);
            this.pictureColor.Name = "pictureColor";
            this.pictureColor.Size = new System.Drawing.Size(53, 31);
            this.pictureColor.TabIndex = 0;
            this.pictureColor.UseVisualStyleBackColor = false;
            // 
            // pic
            // 
            this.pic.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pic.Location = new System.Drawing.Point(87, 24);
            this.pic.Name = "pic";
            this.pic.Size = new System.Drawing.Size(1097, 637);
            this.pic.TabIndex = 2;
            this.pic.TabStop = false;
            this.pic.Paint += new System.Windows.Forms.PaintEventHandler(this.pic_Paint);
            this.pic.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pic_MouseClick);
            this.pic.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pic_MouseDown);
            this.pic.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pic_MouseMove);
            this.pic.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pic_MouseUp);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1184, 24);
            this.menuStrip1.TabIndex = 3;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newToolStripMenuItem,
            this.openToolStripMenuItem,
            this.toolStripSeparator,
            this.saveToolStripMenuItem,
            this.toolStripSeparator1,
            this.toolStripSeparator2});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // newToolStripMenuItem
            // 
            this.newToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("newToolStripMenuItem.Image")));
            this.newToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.newToolStripMenuItem.Name = "newToolStripMenuItem";
            this.newToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.newToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.newToolStripMenuItem.Text = "&New";
            this.newToolStripMenuItem.Click += new System.EventHandler(this.newToolStripMenuItem_Click);
            // 
            // openToolStripMenuItem
            // 
            this.openToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("openToolStripMenuItem.Image")));
            this.openToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.openToolStripMenuItem.Name = "openToolStripMenuItem";
            this.openToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
            this.openToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.openToolStripMenuItem.Text = "&Open";
            this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // toolStripSeparator
            // 
            this.toolStripSeparator.Name = "toolStripSeparator";
            this.toolStripSeparator.Size = new System.Drawing.Size(177, 6);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Image = ((System.Drawing.Image)(resources.GetObject("saveToolStripMenuItem.Image")));
            this.saveToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.saveToolStripMenuItem.Text = "&Save";
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.saveToolStripMenuItem_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(177, 6);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(177, 6);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1184, 661);
            this.Controls.Add(this.pic);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pic)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnLine;
        private System.Windows.Forms.Button btnRectangle;
        private System.Windows.Forms.Button btnEllipse;
        private System.Windows.Forms.Button btnEraser;
        private System.Windows.Forms.Button btnPencil;
        private System.Windows.Forms.Button btnFill;
        private System.Windows.Forms.Button btnColor;
        private System.Windows.Forms.Button pictureColor;
        private System.Windows.Forms.PictureBox pic;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
    }
}

