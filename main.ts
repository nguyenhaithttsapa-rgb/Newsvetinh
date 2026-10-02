Deno.serve(async (req) => {
  const url = new URL(req.url);
  const path = url.pathname === "/" ? "/index.html" : url.pathname;
  try {
    const file = await Deno.readFile("." + path);
    const contentType = path.endsWith(".html") ? "text/html; charset=utf-8" :
                        path.endsWith(".json") ? "application/json" :
                        path.endsWith(".xml") ? "application/xml" :
                        path.endsWith(".txt") ? "text/plain" : "text/html; charset=utf-8";
    return new Response(file, { headers: { "content-type": contentType } });
  } catch (_e) {
    const file = await Deno.readFile("./index.html");
    return new Response(file, { headers: { "content-type": "text/html; charset=utf-8" } });
  }
});
