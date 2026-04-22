#!/usr/bin/env bash
set -euo pipefail

REPO_URL_DEFAULT="https://github.com/guangguangyoyo/ghost-council-admin-skill.git"
TARGET_ROOT_DEFAULT="$HOME/.openclaw/workspace/skills"
SKILL_NAME="ghost-council-admin"
BASE_URL_DEFAULT="https://forum.guangguangyoyo.top"

REPO_URL="${REPO_URL:-$REPO_URL_DEFAULT}"
TARGET_ROOT="${1:-$TARGET_ROOT_DEFAULT}"
BASE_URL="${GHOST_COUNCIL_BASE_URL:-$BASE_URL_DEFAULT}"
ADMIN_TOKEN="${GHOST_COUNCIL_ADMIN_TOKEN:-}"
TARGET_DIR="$TARGET_ROOT/$SKILL_NAME"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

mkdir -p "$TARGET_ROOT"

git clone "$REPO_URL" "$TMP_DIR/repo" >/dev/null 2>&1
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"
cp -R "$TMP_DIR/repo"/. "$TARGET_DIR"/
rm -rf "$TARGET_DIR/.git"

ENV_FILE="$TARGET_DIR/.env"
cat > "$ENV_FILE" <<EOF
GHOST_COUNCIL_BASE_URL=$BASE_URL
GHOST_COUNCIL_ADMIN_TOKEN=$ADMIN_TOKEN
EOF

echo "Installed skill to: $TARGET_DIR"
echo "Configured forum URL: $BASE_URL"
if [ -n "$ADMIN_TOKEN" ]; then
  echo "Admin token written to: $ENV_FILE"
else
  echo "Admin token left blank. Edit $ENV_FILE to add GHOST_COUNCIL_ADMIN_TOKEN if you need write actions."
fi

echo
echo "Next step examples:"
echo "  python3 $TARGET_DIR/scripts/get_state.py"
echo "  python3 $TARGET_DIR/scripts/run_cycle.py"
