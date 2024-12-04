import "./globals.css";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Next API & Fast API",
  description: "Next.js and FastAPI working together",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      {/* <head>
        <meta charSet="UTF-8" />
      </head> */}
      <body className={inter.className}>{children}</body>
    </html>
  );
}
