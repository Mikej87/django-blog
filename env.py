import os

# Notice: No colon at the end, and fixed the @ symbol area
os.environ.setdefault("DATABASE_URL", "postgres://u809kcl8m7mmfu:p"\
"29e152d2437f9995777dffba050e3ab5dc6e94e7a9a63fa8185ab3ea3d84db10@cbh"\
"nv71uilek74.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com/d8nf982i8nquve")

os.environ.setdefault("SECRET_KEY", "your-unique-secret-key-12345")

os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://<your_api_key>:<your_api_secret>@dd6bxy9wa")





